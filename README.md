# z-image api SDK for RunAPI

The z-image api SDK packages JavaScript, Ruby, and Go clients for Z-Image on RunAPI. Use this z-image api SDK for text-to-image, image-to-image, edit, and creative production workflows that need typed installs, JSON request bodies, task polling, and consistent RunAPI errors across services.

Z-Image belongs to the Alibaba catalog on RunAPI. The public model page is https://runapi.ai/models/z-image; variant pages below carry pricing, rate-limit, and commercial-usage details. The public `z-image-sdk` repository groups the JavaScript, Ruby, and Go packages for this model.

## Install

```bash
npm install @runapi.ai/z-image
gem install runapi-z-image
go get github.com/runapi-ai/z-image-sdk/go@latest
```

## What you can build

- Build product imagery, creative automation, design previews, and agent image workflows with the z-image api SDK.
- Keep one model-specific repository while installing only the language package your app needs.
- Use `create` for submit-only jobs, `get` for status lookup, and `run` for submit-and-poll scripts.
- Handle authentication, validation, rate limits, insufficient credits, task failures, and polling timeouts through RunAPI SDK errors.

The JavaScript client exposes generations resources, and the Ruby and Go packages mirror the same RunAPI task lifecycle.

## JavaScript quick start

```typescript
import { ZImageClient } from '@runapi.ai/z-image';

const client = new ZImageClient();

const task = await client.generations.create({
  // Pass the Z-Image request body documented at https://runapi.ai/docs#z-image.
});

const status = await client.generations.get(task.id);
```

For short scripts, use `run` with the same JSON body to create the task and wait for completion. For web request handlers, prefer `create` plus webhook or later `get` polling so the server does not hold a worker open.

## Repository layout

- `js/` publishes `@runapi.ai/z-image`.
- `ruby/` publishes `runapi-z-image` when RubyGems publishing resumes.
- `go/` publishes `github.com/runapi-ai/z-image-sdk/go` and depends on `github.com/runapi-ai/core-sdk/go`.

## Public links

- Model page: https://runapi.ai/models/z-image
- SDK docs: https://runapi.ai/docs#sdk-z-image
- Product docs: https://runapi.ai/docs#z-image
- SDK repository: https://github.com/runapi-ai/z-image-sdk
- Skill repository: https://github.com/runapi-ai/z-image
- Provider comparison: https://runapi.ai/providers/alibaba
- Full catalog: https://runapi.ai/models

## Pricing and variants

Use the most specific z-image api variant page for pricing, rate limits, and commercial usage:
- [Z Image](https://runapi.ai/models/z-image)

Default pricing link for the z-image api SDK: https://runapi.ai/models/z-image

## FAQ

### Which package should I install for z-image api work?

Install the model package for your language: `@runapi.ai/z-image`, `runapi-z-image`, or `github.com/runapi-ai/z-image-sdk/go`. Install core SDK packages only when you are building shared SDK infrastructure.

### Where should public links point?

Primary z-image api links point to https://runapi.ai/models/z-image. Pricing and usage-policy links point to variant pages such as https://runapi.ai/models/z-image. Provider comparisons point to https://runapi.ai/providers/alibaba, and broad browsing points to https://runapi.ai/models.

## License

Licensed under the Apache License, Version 2.0.
