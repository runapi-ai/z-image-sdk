"""Z-Image client."""

from __future__ import annotations

from typing import Any, Optional

from runapi.core import ProviderClient

from .resources.text_to_image import TextToImage


class ZImageClient(ProviderClient):
    """Z-Image text-to-image client.

    Example::

        client = ZImageClient(api_key="sk-...")
        result = client.text_to_image.run(
            model="z-image", prompt="A neon city street", aspect_ratio="1:1"
        )
    """

    def __init__(self, api_key: Optional[str] = None, **options: Any) -> None:
        super().__init__(api_key, **options)
        http = self._http
        self.text_to_image = TextToImage(http)
