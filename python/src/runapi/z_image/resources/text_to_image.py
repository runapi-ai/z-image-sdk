"""Z-Image text-to-image resource."""

from __future__ import annotations

from typing import Any

from runapi.core import Resource

from ..contract_gen import CONTRACT
from ..types import (
    CompletedTextToImageResponse,
    TextToImageResponse,
)


class TextToImage(Resource):
    """Generate images from text prompts with Z-Image."""

    ENDPOINT = "/api/v1/z_image/text_to_image"

    RESPONSE_CLASS = TextToImageResponse
    COMPLETED_RESPONSE_CLASS = CompletedTextToImageResponse

    def run(self, **params: Any) -> Any:
        """Create a text-to-image task and poll until it completes.

        Args:
            **params: text-to-image parameters (model, ...).

        Returns:
            The completed (narrowed) text-to-image response.
        """
        task = self.create(**params)
        return self._poll_until_complete(lambda: self.get(task.id))

    def create(self, **params: Any) -> Any:
        """Create a text-to-image task and return immediately with an id.

        Args:
            **params: text-to-image parameters (model, ...).

        Returns:
            The task creation result with an id.
        """
        compacted = self._compact_params(params)
        self._validate_contract(CONTRACT["text-to-image"], compacted)
        return self._request("post", self.ENDPOINT, body=compacted)

    def get(self, id: str) -> Any:
        """Fetch the current status of a text-to-image task.

        Args:
            id: The task id returned by ``create``.

        Returns:
            The current task status.
        """
        return self._request("get", f"{self.ENDPOINT}/{id}")
