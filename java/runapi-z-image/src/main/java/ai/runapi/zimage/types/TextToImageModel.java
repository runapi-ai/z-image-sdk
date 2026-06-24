package ai.runapi.zimage.types;

import com.fasterxml.jackson.annotation.JsonCreator;

/** Model slug for text to image operations. */
public final class TextToImageModel extends ZimageValue {
  /** z-image model slug. */
  public static final TextToImageModel Z_IMAGE = new TextToImageModel("z-image");

  /** Creates a model value from a literal model slug. */
  @JsonCreator
  public TextToImageModel(String value) {
    super(value);
  }
}
