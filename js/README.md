# Z-Image API JavaScript SDK for RunAPI

The z-image api JavaScript SDK is the language-specific package for Z-Image on RunAPI. Use this z-image api package for text-to-image, image editing, and creative production flows when your application needs JSON request bodies, task status lookup, and consistent RunAPI errors in JavaScript.

This z-image api README is the JavaScript package guide inside the public `z-image-sdk` repository. For the repository overview, start at `../README.md`; for model details, use https://runapi.ai/models/z-image; for API reference, use https://runapi.ai/docs#z-image; for SDK docs, use https://runapi.ai/docs#sdk-z-image.

## Install

```bash
npm install @runapi.ai/z-image
```

## Quick start

```typescript
import { ZImageClient } from '@runapi.ai/z-image';

const client = new ZImageClient();
const task = await client.generations.create({
  // Pass the Z-Image JSON request body from https://runapi.ai/docs#z-image.
});
const status = await client.generations.get(task.id);
```

Use `create` when you want to submit a task and return quickly, `get` when you need the latest task state, and `run` when a script should create and poll until completion. In web request handlers, prefer `create` plus webhook or later `get` polling so a worker is not held open.

## Language notes

Use the TypeScript types in `src/types.ts` and the resource classes under `src/resources` when building image applications. The available resources include generations. Keep `RUNAPI_API_KEY` in the environment or your secret manager; never commit API keys or callback secrets.

## Links

- Model page: https://runapi.ai/models/z-image
- SDK docs: https://runapi.ai/docs#sdk-z-image
- Product docs: https://runapi.ai/docs#z-image
- Pricing and rate limits: https://runapi.ai/models/z-image
- Provider comparison: https://runapi.ai/providers/alibaba
- Full catalog: https://runapi.ai/models
- Repository: https://github.com/runapi-ai/z-image-sdk

## License

Licensed under the Apache License, Version 2.0.
