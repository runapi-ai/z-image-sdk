# frozen_string_literal: true

require "spec_helper"

RSpec.describe RunApi::ZImage::Client do
  before do
    allow(ConnectionPool).to receive(:new).and_return(instance_double(ConnectionPool))
  end

  after { RunApi.api_key = nil }

  it "accepts api_key as parameter" do
    client = described_class.new(api_key: "param-key")
    expect(client).to be_a(described_class)
  end

  it "exposes text_to_image accessor" do
    client = described_class.new(api_key: "test-key")
    expect(client.text_to_image).to be_a(RunApi::ZImage::Resources::TextToImage)
  end
end
