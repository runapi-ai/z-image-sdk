# frozen_string_literal: true

module RunApi
  module ZImage
    module Types
      MODELS = %w[z-image].freeze
      ASPECT_RATIOS = %w[1:1 4:3 3:4 16:9 9:16].freeze

      class Image < RunApi::Core::BaseModel
        optional :url, String
      end

      class TextToImageResponse < RunApi::Core::TaskResponse
        required :id, String
        optional :status, String, enum: -> { RunApi::Core::TaskResponse::Status::ALL }
        optional :images, [ -> { Image } ]
        optional :error, String
      end

      class CompletedTextToImageResponse < TextToImageResponse
        required :images, [ -> { Image } ]
      end
    end
  end
end
