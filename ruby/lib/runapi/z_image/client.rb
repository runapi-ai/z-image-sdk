# frozen_string_literal: true

module RunApi
  module ZImage
    # Z-Image text-to-image generation client.
    #
    # @example
    #   client = RunApi::ZImage::Client.new(api_key: "sk-...")
    #   result = client.text_to_image.run(
    #     model: "z-image",
    #     prompt: "A serene Japanese garden at sunrise",
    #     aspect_ratio: "16:9"
    #   )
    #   puts result.images.first.url
    class Client < RunApi::Core::Client
      # @return [Resources::TextToImage] Text-to-image generation with configurable aspect ratio and safety filtering.
      attr_reader :text_to_image

      def initialize(api_key: nil, **options)
        super
        @text_to_image = Resources::TextToImage.new(http)
      end
    end
  end
end
