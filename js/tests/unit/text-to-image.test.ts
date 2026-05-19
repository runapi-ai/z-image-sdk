import { describe, it, expect, vi, beforeEach } from 'vitest';
import { TextToImage } from '../../src/resources/text-to-image';
import type { HttpClient } from '@runapi.ai/core';
import type { TextToImageResponse, TaskCreateResponse } from '../../src/types';

describe('TextToImage', () => {
  const mockHttp: HttpClient = { request: vi.fn() };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('sends POST /api/v1/z_image/text_to_image with flat params', async () => {
    const mockResponse: TaskCreateResponse = { id: 'task-123', status: 'processing' };
    vi.mocked(mockHttp.request).mockResolvedValueOnce(mockResponse);

    const textToImage = new TextToImage(mockHttp);
    const result = await textToImage.create({
      model: 'z-image',
      prompt: 'A Paris cafe',
      aspect_ratio: '1:1',
      nsfw_checker: true,
    });

    expect(mockHttp.request).toHaveBeenCalledWith('POST', '/api/v1/z_image/text_to_image', {
      body: {
        model: 'z-image',
        prompt: 'A Paris cafe',
        aspect_ratio: '1:1',
        nsfw_checker: true,
      },
    });
    expect(result).toEqual(mockResponse);
  });

  it('sends GET /api/v1/z_image/text_to_image/:id', async () => {
    const mockResponse: TextToImageResponse = {
      id: 'task-123',
      status: 'completed',
      images: [{ url: 'https://file.runapi.ai/out.png' }],
    };
    vi.mocked(mockHttp.request).mockResolvedValueOnce(mockResponse);

    const textToImage = new TextToImage(mockHttp);
    const result = await textToImage.get('task-123');

    expect(mockHttp.request).toHaveBeenCalledWith('GET', '/api/v1/z_image/text_to_image/task-123', {});
    expect(result).toEqual(mockResponse);
  });
});
