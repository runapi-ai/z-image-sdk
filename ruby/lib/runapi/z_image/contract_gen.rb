# frozen_string_literal: true

module RunApi
  module ZImage
    CONTRACT = {
      "text-to-image" => {
        "models" => ["z-image"],
        "fields_by_model" => {
          "z-image" => {
            "aspect_ratio" => {
              "enum" => ["1:1", "4:3", "3:4", "16:9", "9:16"],
              "required" => true
            },
            "prompt" => {
              "required" => true,
              "min" => 1,
              "max" => 1000,
              "length" => true
            }
          }
        }
      }
    }.freeze
  end
end
