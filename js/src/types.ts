import type { AsyncTaskStatus } from '@runapi.ai/core';

export type ZImageModel = 'z-image';
export type AspectRatio = '1:1' | '4:3' | '3:4' | '16:9' | '9:16';

export interface TextToImageParams {
  model: ZImageModel;
  prompt: string;
  aspect_ratio: AspectRatio;
  nsfw_checker?: boolean;
  callback_url?: string;
}

export interface TaskCreateResponse {
  id: string;
  status?: 'processing';
}

export interface Image {
  url: string;
}

export interface TextToImageResponse {
  id: string;
  status: AsyncTaskStatus;
  images?: Image[];
  error?: string;
  [key: string]: unknown;
}

export type CompletedTextToImageResponse = TextToImageResponse & {
  status: 'completed';
  images: Image[];
};
