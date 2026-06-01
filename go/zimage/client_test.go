package zimage

import (
	"context"
	"encoding/json"
	"testing"

	"github.com/runapi-ai/core-sdk/go/core"
)

type stubHTTPClient struct {
	method   string
	path     string
	body     any
	response json.RawMessage
}

func (s *stubHTTPClient) Request(_ context.Context, method, path string, opts *core.HTTPRequestOptions) (json.RawMessage, error) {
	s.method = method
	s.path = path
	if opts != nil {
		s.body = opts.Body
	}
	return s.response, nil
}

func TestTextToImageCreate(t *testing.T) {
	stub := &stubHTTPClient{response: json.RawMessage(`{"id":"task_123","status":"processing"}`)}
	client := NewClientWithHTTP(stub)
	enableSafetyChecker := true
	resp, err := client.TextToImage.Create(context.Background(), TextToImageParams{
		Model:               "z-image",
		Prompt:              "A Paris cafe",
		AspectRatio:         "1:1",
		EnableSafetyChecker: &enableSafetyChecker,
	})
	if err != nil {
		t.Fatal(err)
	}
	if stub.method != "POST" || stub.path != "/api/v1/z_image/text_to_image" {
		t.Fatalf("unexpected request: %s %s", stub.method, stub.path)
	}
	body := stub.body.(map[string]any)
	if body["model"] != "z-image" || body["prompt"] != "A Paris cafe" || body["aspect_ratio"] != "1:1" || body["enable_safety_checker"] != true {
		t.Fatalf("unexpected body: %v", body)
	}
	if resp.ID != "task_123" {
		t.Fatalf("unexpected task ID: %v", resp.ID)
	}
}

func TestTextToImageGet(t *testing.T) {
	stub := &stubHTTPClient{response: json.RawMessage(`{"id":"task_456","status":"completed","images":[{"url":"https://cdn.runapi.ai/public/samples/result.jpg"}]}`)}
	client := NewClientWithHTTP(stub)
	resp, err := client.TextToImage.Get(context.Background(), "task_abc")
	if err != nil {
		t.Fatal(err)
	}
	if stub.method != "GET" || stub.path != "/api/v1/z_image/text_to_image/task_abc" {
		t.Fatalf("unexpected request: %s %s", stub.method, stub.path)
	}
	if resp.ID != "task_456" || string(resp.Status) != "completed" {
		t.Fatalf("unexpected response: %+v", resp)
	}
	if len(resp.Images) != 1 || resp.Images[0].URL != "https://cdn.runapi.ai/public/samples/result.jpg" {
		t.Fatalf("unexpected images: %v", resp.Images)
	}
}
