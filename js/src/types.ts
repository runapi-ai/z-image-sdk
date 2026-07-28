import type { AsyncTaskStatus, TaskBillingResponse, TaskResponse } from '@runapi.ai/core';

/** Z-Image model slug. */
export type ZImageModel = 'z-image';
/** Output aspect ratio controlling the generated image dimensions. */
export type AspectRatio = '1:1' | '4:3' | '3:4' | '16:9' | '9:16';

/**
 * Parameters for text-to-image generation. `model`, `prompt`, and `aspect_ratio`
 * are all required.
 */
export interface TextToImageParams {
  model: ZImageModel;
  /** Text description of the desired image, up to 1 000 characters. */
  prompt: string;
  /** Controls the output image dimensions. */
  aspect_ratio: AspectRatio;
  /** Toggle content safety filtering. Defaults to enabled when omitted. */
  enable_safety_checker?: boolean;
  /** HTTPS callback URL for task completion notification. */
  callback_url?: string;
}

/** Acknowledgement returned by `create()` before the task starts processing. */
export interface TaskCreateResponse extends TaskBillingResponse {
  id: string;
  status?: 'processing';
}

/** URL to a generated image. */
export interface Image {
  url: string;
}

/** Async text-to-image task result with lifecycle status. */
export interface TextToImageResponse extends TaskResponse {
  id: string;
  status: AsyncTaskStatus;
  /** Generated image files; populated once the task completes. */
  images?: Image[];
  error?: string;
  [key: string]: unknown;
}

/** Narrowed response returned by `run()` once polling confirms completion. Images are guaranteed present. */
export type CompletedTextToImageResponse = TextToImageResponse & {
  status: 'completed';
  images: Image[];
};
