# frozen_string_literal: true

module RunApi
  module ZImage
    # Response models for the Z-Image text-to-image API.
    module Types
      # URL to a generated image.
      class Image < RunApi::Core::BaseModel
        optional :url, String
      end

      # Async text-to-image task result with lifecycle status.
      class TextToImageResponse < RunApi::Core::TaskResponse
        required :id, String
        optional :status, String, enum: -> { RunApi::Core::TaskResponse::Status::ALL }
        optional :images, [-> { Image }]
        optional :error, String
      end

      # Narrowed response returned by +run+ once polling confirms completion.
      # Images are guaranteed present.
      class CompletedTextToImageResponse < TextToImageResponse
        required :images, [-> { Image }]
      end
    end
  end
end
