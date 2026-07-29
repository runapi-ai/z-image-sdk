# Z-Image Python SDK for RunAPI

The Z-Image Python SDK is the language-specific package for Z-Image on RunAPI. Use this package for image generation, image editing, and creative production workflows when your application needs request bodies, task status lookup, and consistent RunAPI errors in Python.

This README is the Python package guide inside the public `z-image-sdk` repository. For the repository overview, start at `../README.md`; for model details, use https://runapi.ai/models/z-image; for API reference, use https://runapi.ai/docs/api/z-image/text-to-image; for SDK docs, use https://runapi.ai/docs/resources/sdks.

## Install

```bash
pip install runapi-z-image
```

## Quick start

```python
from runapi.z_image import ZImageClient

client = ZImageClient()  # reads RUNAPI_API_KEY, or pass api_key="sk-..."

task = client.text_to_image.create(
    model="z-image",
    prompt="A neon city street after rain, cinematic",
    aspect_ratio="16:9",
)
status = client.text_to_image.get(task.id)
```

Use `create` to submit a task and return quickly, `get` to fetch the latest task state, and `run` when a script should create and poll until completion:

```python
result = client.text_to_image.run(
    model="z-image",
    prompt="A serene mountain lake at dawn",
    aspect_ratio="1:1",
)
print(result.images[0].url)
```

In web request handlers, prefer `create` plus webhook or later `get` polling so a worker is not held open.

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## Language notes

Pass parameters as keyword arguments and catch the `runapi.z_image` error classes when building image jobs or scripts. The available resource is `text_to_image`. Keep `RUNAPI_API_KEY` in the environment or your secret manager; never commit API keys or callback secrets.

## Links

- Model page: https://runapi.ai/models/z-image
- SDK docs: https://runapi.ai/docs/resources/sdks
- Product docs: https://runapi.ai/docs/api/z-image/text-to-image
- Pricing and rate limits: https://runapi.ai/models/z-image
- Provider comparison: https://runapi.ai/providers/alibaba
- Full catalog: https://runapi.ai/models
- Repository: https://github.com/runapi-ai/z-image-sdk

## License

Licensed under the Apache License, Version 2.0.
