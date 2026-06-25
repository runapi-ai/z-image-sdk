"""Z-Image response models."""

from __future__ import annotations

from runapi.core import BaseModel, TaskResponse, optional, required


class Image(BaseModel):
    url = optional(str)


class TextToImageResponse(TaskResponse):
    """Z-Image text-to-image task status response."""

    id = required(str)
    status = optional(str, enum=lambda: TaskResponse.Status.ALL)
    images = optional([lambda: Image])
    error = optional(str)


class CompletedTextToImageResponse(TextToImageResponse):
    """Narrowed response from ``run()`` once polling observes completion."""

    images = required([lambda: Image])
