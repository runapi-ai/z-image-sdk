<p align="center">
  <a href="https://github.com/runapi-ai/z-image">
    <h3 align="center">Z-Image API Skill for RunAPI</h3>
  </a>
</p>

<p align="center">
  Install this agent skill, inspect Z-Image fields, then run jobs through the RunAPI CLI.
</p>

<p align="center">
  <a href="https://runapi.ai/models/z-image"><strong>Model Reference</strong></a> · <a href="https://github.com/runapi-ai/cli"><strong>CLI</strong></a> · <a href="https://github.com/runapi-ai/z-image-sdk"><strong>SDK</strong></a>
</p>

<div align="center">

[![skills.sh](https://www.skills.sh/b/runapi-ai/z-image)](https://www.skills.sh/runapi-ai/z-image/z-image)
[![ClawHub](https://img.shields.io/badge/ClawHub-runapi--z--image-111827)](https://clawhub.ai/runapi-ai/runapi-z-image)
[![License](https://img.shields.io/github/license/runapi-ai/z-image)](https://github.com/runapi-ai/z-image/blob/main/LICENSE)

</div>
<br/>

Generate images with Z-Image text-to-image. This skill helps Claude Code, Codex, Gemini CLI, Cursor, and 50+ agents integrate Z-Image through RunAPI.

The canonical agent file is `skills/z-image/SKILL.md`.

## Install

```bash
npx skills add runapi-ai/z-image -g
```

Or paste this prompt to your AI agent:

```text
Install the z-image skill for me:

1. Clone https://github.com/runapi-ai/z-image
2. Copy the skills/z-image/ directory into your
   user-level skills directory (e.g. ~/.claude/skills/
   for Claude Code, ~/.codex/skills/ for Codex).
3. Verify that SKILL.md is present.
4. Confirm the install path when done.
```

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

## Agent rules

- Keep API keys in `RUNAPI_API_KEY` or RunAPI CLI config; never commit secrets.
- Prefer `create`, `get`, and `run` JSON passthrough patterns instead of inventing flags for every model parameter.
- For z-image api pricing, rate-limit, and commercial-usage answers, link to the model page rather than the repository README.

## License

Licensed under the Apache License, Version 2.0.
