import { describe, it, expect, beforeEach, afterAll } from 'vitest';
import { AuthenticationError } from '@runapi.ai/core';
import { ZImageClient } from '../../src';

const originalEnv = process.env.RUNAPI_API_KEY;

describe('ZImageClient', () => {
  beforeEach(() => {
    delete process.env.RUNAPI_API_KEY;
  });

  afterAll(() => {
    if (originalEnv === undefined) {
      delete process.env.RUNAPI_API_KEY;
    } else {
      process.env.RUNAPI_API_KEY = originalEnv;
    }
  });

  it('initializes with an API key', () => {
    const client = new ZImageClient({ apiKey: 'test-key' });
    expect(client.textToImage).toBeDefined();
  });

  it('throws when apiKey missing and env unset', () => {
    expect(() => new ZImageClient()).toThrow(AuthenticationError);
  });

  it('exposes textToImage resource', () => {
    const client = new ZImageClient({ apiKey: 'test-key' });
    expect(typeof client.textToImage.run).toBe('function');
    expect(typeof client.textToImage.create).toBe('function');
    expect(typeof client.textToImage.get).toBe('function');
  });
});
