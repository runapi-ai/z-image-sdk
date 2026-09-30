import pytest

from runapi.core import ApiResponse, RequestOptions, config
from runapi.core.errors import AuthenticationError
from runapi.z_image import ZImageClient
from runapi.z_image.resources.text_to_image import TextToImage
from runapi.z_image.types import CompletedTextToImageResponse, TextToImageResponse


class FakeHttp:
    def __init__(self, *responses):
        self._responses = list(responses)
        self.calls = []
        self.options = []

    def request(self, method, path, body=None, options=None):
        self.calls.append((method, path, body))
        self.options.append(options)
        if self._responses:
            return self._responses.pop(0)
        return {"id": "task_1", "status": "pending"}


@pytest.fixture(autouse=True)
def reset_config(monkeypatch):
    monkeypatch.delenv("RUNAPI_API_KEY", raising=False)
    monkeypatch.setattr(config, "api_key", None)
    yield


# --- auth -----------------------------------------------------------------


def test_accepts_api_key_parameter():
    assert isinstance(ZImageClient(api_key="k", http_client=FakeHttp()), ZImageClient)


def test_falls_back_to_global(monkeypatch):
    monkeypatch.setattr(config, "api_key", "global-key")
    assert isinstance(ZImageClient(http_client=FakeHttp()), ZImageClient)


def test_falls_back_to_env(monkeypatch):
    monkeypatch.setenv("RUNAPI_API_KEY", "env-key")
    assert isinstance(ZImageClient(http_client=FakeHttp()), ZImageClient)


def test_raises_without_api_key():
    with pytest.raises(AuthenticationError, match="API key is required"):
        ZImageClient()


# --- injection / accessors ------------------------------------------------


def test_uses_injected_http_client():
    fake = FakeHttp()
    client = ZImageClient(api_key="k", http_client=fake)
    assert client.text_to_image._http is fake


def test_exposes_resource_accessors():
    client = ZImageClient(api_key="k", http_client=FakeHttp())
    assert isinstance(client.text_to_image, TextToImage)


# --- request shapes -------------------------------------------------------


def test_create_posts_compacted_body():
    fake = FakeHttp({"id": "t1", "status": "pending"})
    client = ZImageClient(api_key="k", http_client=fake)
    result = client.text_to_image.create(
        model="z-image", prompt="hello world", aspect_ratio="1:1", seed=None
    )
    assert fake.calls == [
        ("post", "/api/v1/z_image/text_to_image", {"model": "z-image", "prompt": "hello world", "aspect_ratio": "1:1"})]
    assert isinstance(result, TextToImageResponse)


def test_create_passes_request_options_and_retains_response_headers():
    fake = FakeHttp(ApiResponse({"id": "t1", "status": "pending"}, {"X-RunAPI-Task-Id": "task-ref-1"}))
    client = ZImageClient(api_key="k", http_client=fake)
    options = RequestOptions(headers={"X-Client-Request-Id": "req-123"})

    result = client.text_to_image.create(
        model="z-image",
        prompt="hello world",
        aspect_ratio="1:1",
        options=options,
    )

    assert fake.options == [options]
    assert result.runapi_task_id == "task-ref-1"
    assert result.response_headers["X-RunAPI-Task-Id"] == "task-ref-1"


def test_get_fetches_by_id():
    fake = FakeHttp({"id": "t1", "status": "processing"})
    client = ZImageClient(api_key="k", http_client=fake)
    client.text_to_image.get("t1")
    assert fake.calls == [("get", "/api/v1/z_image/text_to_image/t1", None)]


def test_get_passes_request_options():
    options = RequestOptions(headers={"X-Client-Request-Id": "req-123"})
    fake = FakeHttp({"id": "t1", "status": "processing"})
    client = ZImageClient(api_key="k", http_client=fake)
    client.text_to_image.get("t1", options=options)
    assert fake.options == [options]


def test_run_narrows_completed_type():
    fake = FakeHttp(
        {"id": "t1", "status": "pending"},
        {"id": "t1", "status": "completed", "usage": {"cost": 0.05}, "images": [{"url": "https://x/y.png"}]},
    )
    client = ZImageClient(api_key="k", http_client=fake)
    result = client.text_to_image.run(model="z-image", prompt="a serene lake", aspect_ratio="1:1")
    assert isinstance(result, CompletedTextToImageResponse)
    assert result.images[0].url == "https://x/y.png"


def test_run_passes_request_options_and_retains_completed_response_headers():
    options = RequestOptions(headers={"X-Client-Request-Id": "req-123"})
    fake = FakeHttp(
        ApiResponse({"id": "t1", "status": "pending"}, {"X-RunAPI-Task-Id": "task-ref-create"}),
        ApiResponse(
            {"id": "t1", "status": "completed", "usage": {"cost": 0.05}, "images": [{"url": "https://x/y.png"}]},
            {"X-RunAPI-Task-Id": "task-ref-complete"},
        ),
    )
    client = ZImageClient(api_key="k", http_client=fake)
    result = client.text_to_image.run(
        model="z-image",
        prompt="a serene lake",
        aspect_ratio="1:1",
        options=options,
    )
    assert fake.options == [options, options]
    assert isinstance(result, CompletedTextToImageResponse)
    assert result.runapi_task_id == "task-ref-complete"
