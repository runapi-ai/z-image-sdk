# Z-Image API Skill for RunAPI

Generate images with Z-Image text-to-image. This skill helps Claude Code, Codex, Gemini CLI, Cursor, and 50+ agents integrate Z-Image through RunAPI.

The canonical agent file is `skills/z-image/SKILL.md`.

## Install

```bash
npx skills add runapi-ai/z-image -g
```

Or manually: clone this repo and copy `skills/z-image/` into your agent's skills directory.

## Quick example

```typescript
import { ZImageClient } from '@runapi.ai/z-image';

const client = new ZImageClient();
const result = await client.textToImage.run({
  model: 'z-image',
  prompt: 'A vibrant street market at golden hour',
});
```

## Routing

- Model page: https://runapi.ai/models/z-image
- Product docs: https://runapi.ai/docs#z-image
- SDK docs: https://runapi.ai/docs#sdk-z-image
- SDK repository: https://github.com/runapi-ai/z-image-sdk
- Pricing and rate limits: https://runapi.ai/models/z-image
- Provider comparison: https://runapi.ai/providers/alibaba
- Browse all RunAPI models and skills: https://runapi.ai/models

## Variants

- [Z Image](https://runapi.ai/models/z-image)

## Agent rules

- Keep API keys in `RUNAPI_API_KEY` or RunAPI CLI config; never commit secrets.
- Prefer `create`, `get`, and `run` JSON passthrough patterns instead of inventing flags for every model parameter.
- For z-image api pricing, rate-limit, and commercial-usage answers, link to the variant page rather than the repository README.

## License

Licensed under the Apache License, Version 2.0.
