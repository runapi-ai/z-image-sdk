import { BaseClient, type ClientOptions } from '@runapi.ai/core';
import { TextToImage } from './resources/text-to-image';

/**
 * Z-Image text-to-image generation client.
 *
 * @example
 * ```typescript
 * import { ZImageClient } from '@runapi.ai/z-image';
 * const client = new ZImageClient({ apiKey: 'sk-...' });
 * const result = await client.textToImage.run({
 *   model: 'z-image',
 *   prompt: 'A serene Japanese garden at sunrise',
 *   aspect_ratio: '16:9',
 * });
 * console.log(result.images[0].url);
 * ```
 */
export class ZImageClient extends BaseClient {
  /** Generates images from text prompts with configurable aspect ratio and safety filtering. */
  public readonly textToImage: TextToImage;

  constructor(options: ClientOptions = {}) {
    super(options);
    this.textToImage = new TextToImage(this.http);
  }
}
