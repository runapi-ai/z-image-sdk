"""Z-Image client."""

from __future__ import annotations

from typing import Any, Optional

from runapi.core import ClientOptions, HttpClient, resolve_api_key

from .resources.text_to_image import TextToImage


class ZImageClient:
    """Z-Image text-to-image client.

    Example::

        client = ZImageClient(api_key="sk-...")
        result = client.text_to_image.run(
            model="z-image", prompt="A neon city street", aspect_ratio="1:1"
        )
    """

    def __init__(self, api_key: Optional[str] = None, **options: Any) -> None:
        resolved_api_key = resolve_api_key(api_key)
        client_options = ClientOptions(api_key=resolved_api_key, **options)
        http = client_options.http_client or HttpClient(client_options)
        self.text_to_image = TextToImage(http)
