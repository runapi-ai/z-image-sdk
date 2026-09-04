<p align="center">
  <a href="https://runapi.ai"><img src="https://runapi.ai/icon.svg" height="56" alt="RunAPI"></a>
</p>

<h3 align="center">
  <a href="https://github.com/runapi-ai/z-image-sdk">Z-Image API SDK for RunAPI</a>
</h3>

<p align="center">
  Z-Image API SDKs for JavaScript, Python, Ruby, Go, Java, and PHP on RunAPI.
</p>

<div align="center">

[![npm](https://img.shields.io/npm/v/@runapi.ai/z-image)](https://www.npmjs.com/package/@runapi.ai/z-image)
[![PyPI](https://img.shields.io/pypi/v/runapi-z-image)](https://pypi.org/project/runapi-z-image/)
[![RubyGems](https://img.shields.io/gem/v/runapi-z-image)](https://rubygems.org/gems/runapi-z-image)
[![Go Reference](https://pkg.go.dev/badge/github.com/runapi-ai/z-image-sdk/go.svg)](https://pkg.go.dev/github.com/runapi-ai/z-image-sdk/go)
[![Maven Central](https://img.shields.io/maven-central/v/ai.runapi/runapi-z-image)](https://central.sonatype.com/artifact/ai.runapi/runapi-z-image)
[![License](https://img.shields.io/github/license/runapi-ai/z-image-sdk)](https://github.com/runapi-ai/z-image-sdk/blob/main/LICENSE)

</div>
<br/>

The Z-Image API SDK packages JavaScript, Python, Ruby, Go, Java, and PHP clients for Z-Image on RunAPI. Use it for text-to-image workflows when your app needs typed request builders, predictable task polling, file upload helpers, account helpers, and consistent RunAPI errors.

Z-Image is listed in the RunAPI model catalog at https://runapi.ai/models/z-image. Variant pages below carry pricing, rate-limit, and commercial-usage details. The public `z-image-sdk` repository groups the non-PHP language packages, examples, CI, and release tags for this model. The PHP package is released from a split Composer repository.

## Install

```bash
npm install @runapi.ai/z-image
pip install runapi-z-image
gem install runapi-z-image
go get github.com/runapi-ai/z-image-sdk/go@latest
```

Gradle:

```kotlin
dependencies {
  implementation("ai.runapi:runapi-z-image:0.1.1")
}
```

Maven:

```xml
<dependency>
  <groupId>ai.runapi</groupId>
  <artifactId>runapi-z-image</artifactId>
  <version>0.1.1</version>
</dependency>
```

Use the Java BOM when installing multiple RunAPI Java modules:

```kotlin
dependencies {
  implementation(platform("ai.runapi:runapi-bom:0.6.2"))
  implementation("ai.runapi:runapi-z-image")
}
```

The PHP package is published from the split Composer repository as `runapi-ai/z-image`; see https://github.com/runapi-ai/z-image-php for PHP install and examples.

## What you can build

- Build apps, agent workflows, batch jobs, and production services around Z-Image requests.
- Install only the language package your app needs while keeping one model-specific repository for docs and releases.
- Use `create` for submit-only jobs, `get` for status lookup, and `run` for submit-and-poll scripts.
- Upload local files, URL files, or base64 files through shared RunAPI file helpers.
- Handle validation, authentication, rate limits, insufficient credits, task failures, and polling timeouts through RunAPI SDK errors.

## Java quick start

```java
import ai.runapi.zimage.ZImageClient;
import ai.runapi.zimage.types.TextToImageParams;
import ai.runapi.zimage.types.CompletedTextToImageResponse;
import ai.runapi.zimage.types.TextToImageModel;

ZImageClient client = ZImageClient.builder()
    .apiKey(System.getenv("RUNAPI_API_KEY"))
    .build();

CompletedTextToImageResponse result = client.textToImage().run(
    TextToImageParams.builder()
        .model(TextToImageModel.Z_IMAGE)
        .prompt("A bilingual poster with crisp typography")
        .aspectRatio("1:1")
        .build()
);
```

Java packages target Java 8 bytecode and are tested on Java 8, 11, 17, and 21. Each model artifact depends on `ai.runapi:runapi-core`, so application code normally installs only `ai.runapi:runapi-z-image`.

## Task lifecycle

Most media endpoints are asynchronous. `create()` submits a task and returns its id, `get(id)` fetches the latest task state, and `run(params)` creates the task and polls until it reaches a terminal state. In web request handlers, prefer `create()` plus webhook or later `get()` polling so the server does not hold a worker open.

## Repository layout

- `js/` publishes `@runapi.ai/z-image`.
- `python/` publishes `runapi-z-image`.
- `ruby/` publishes `runapi-z-image`.
- `go/` publishes `github.com/runapi-ai/z-image-sdk/go` and depends on `github.com/runapi-ai/core-sdk/go`.
- `java/` publishes `ai.runapi:runapi-z-image` and depends on `ai.runapi:runapi-core`.

## Public links

- Model page: https://runapi.ai/models/z-image
- SDK docs: https://runapi.ai/docs/resources/sdks
- Product docs: https://runapi.ai/docs/api/z-image/text-to-image
- SDK repository: https://github.com/runapi-ai/z-image-sdk
- PHP package repository: https://github.com/runapi-ai/z-image-php
- Skill repository: https://github.com/runapi-ai/z-image
- Provider comparison: https://runapi.ai/providers/alibaba
- Full catalog: https://runapi.ai/models

## Pricing and variants

Use the most specific Z-Image variant page for pricing, rate limits, and commercial usage:
- [Z Image](https://runapi.ai/models/z-image)

Default pricing link for the Z-Image SDK: https://runapi.ai/models/z-image

## File storage

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## FAQ

### Which package should I install for Z-Image work?

Install the model package for your language: `@runapi.ai/z-image` on npm, `runapi-z-image` on PyPI, `runapi-z-image` on RubyGems, `github.com/runapi-ai/z-image-sdk/go`, `ai.runapi:runapi-z-image` on Maven Central, or `runapi-ai/z-image` on Packagist. Install core SDK packages only when you are building shared SDK infrastructure.

### Where should public links point?

Primary Z-Image links point to https://runapi.ai/models/z-image. Pricing and usage-policy links point to variant pages such as https://runapi.ai/models/z-image. Provider comparisons point to https://runapi.ai/providers/alibaba, and broad browsing points to https://runapi.ai/models.

## License

Licensed under the Apache License, Version 2.0.
