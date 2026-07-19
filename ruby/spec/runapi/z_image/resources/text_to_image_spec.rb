# frozen_string_literal: true

require "spec_helper"

RSpec.describe RunApi::ZImage::Resources::TextToImage do
  let(:http) { instance_double(RunApi::Core::HttpClient) }
  let(:text_to_image) { described_class.new(http) }
  let(:endpoint) { "/api/v1/z_image/text_to_image" }

  describe "#create" do
    it "POSTs to the correct endpoint with params" do
      params = {model: "z-image", prompt: "A Paris cafe", aspect_ratio: "1:1", enable_safety_checker: true}
      expect(http).to receive(:request).with(:post, endpoint, body: params)
        .and_return("id" => "task-1")

      result = text_to_image.create(**params)
      expect(result).to be_a(RunApi::ZImage::Types::TextToImageResponse)
      expect(result.id).to eq("task-1")
    end

    it "passes request options and exposes response headers" do
      params = {model: "z-image", prompt: "A Paris cafe", aspect_ratio: "1:1"}
      options = RunApi::Core::RequestOptions.new(headers: {"X-Client-Request-Id" => "req-123"})

      expect(http).to receive(:request).with(:post, endpoint, body: params, options: options)
        .and_return(RunApi::Core::Response.new(
          body: {"id" => "task-1"},
          headers: {"X-RunAPI-Task-Id" => "task-ref-1"}
        ))

      result = text_to_image.create(**params, options: options)

      expect(result.id).to eq("task-1")
      expect(result.runapi_task_id).to eq("task-ref-1")
      expect(result.response_headers["X-RunAPI-Task-Id"]).to eq("task-ref-1")
    end

    it "raises ValidationError when required params are missing" do
      expect { text_to_image.create(model: "z-image", prompt: "test") }
        .to raise_error(RunApi::Core::ValidationError, /aspect_ratio is required/)
    end

    it "raises ValidationError for invalid aspect_ratio" do
      expect { text_to_image.create(model: "z-image", prompt: "test", aspect_ratio: "2:3") }
        .to raise_error(RunApi::Core::ValidationError, /aspect_ratio must be one of: 1:1, 4:3, 3:4, 16:9, 9:16/)
    end
  end

  describe "#get" do
    it "GETs the correct endpoint" do
      expect(http).to receive(:request).with(:get, "#{endpoint}/task-1")
        .and_return("id" => "task-1", "status" => "completed", "images" => [{"url" => "https://file.runapi.ai/out.png"}])

      result = text_to_image.get("task-1")
      expect(result).to be_a(RunApi::ZImage::Types::TextToImageResponse)
      expect(result.id).to eq("task-1")
      expect(result.images.first.url).to eq("https://file.runapi.ai/out.png")
    end

    it "passes request options" do
      options = RunApi::Core::RequestOptions.new(headers: {"X-Client-Request-Id" => "req-123"})

      expect(http).to receive(:request).with(:get, "#{endpoint}/task-1", options: options)
        .and_return("id" => "task-1", "status" => "processing")

      text_to_image.get("task-1", options: options)
    end
  end

  describe "#run" do
    it "passes request options to create and get and retains completed response headers" do
      params = {model: "z-image", prompt: "A Paris cafe", aspect_ratio: "1:1"}
      options = RunApi::Core::RequestOptions.new(headers: {"X-Client-Request-Id" => "req-123"})

      expect(http).to receive(:request).with(:post, endpoint, body: params, options: options)
        .and_return(RunApi::Core::Response.new(
          body: {"id" => "task-1", "status" => "pending"},
          headers: {"X-RunAPI-Task-Id" => "task-ref-create"}
        ))
      expect(http).to receive(:request).with(:get, "#{endpoint}/task-1", options: options)
        .and_return(RunApi::Core::Response.new(
          body: {
            "id" => "task-1",
            "status" => "completed",
            "images" => [{"url" => "https://file.runapi.ai/out.png"}]
          },
          headers: {"X-RunAPI-Task-Id" => "task-ref-complete"}
        ))

      result = text_to_image.run(**params, options: options)

      expect(result).to be_a(RunApi::ZImage::Types::CompletedTextToImageResponse)
      expect(result.runapi_task_id).to eq("task-ref-complete")
      expect(result.images.first.url).to eq("https://file.runapi.ai/out.png")
    end
  end
end
