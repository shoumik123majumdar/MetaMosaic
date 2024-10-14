from image_processor import ImageProcessor
import google.generativeai as genai


class GeminiImageProcessor(ImageProcessor):
    """
    Class Implementation of ImageProcessor interface for use with Gemini Models
    """
    def __init__(self, file_path):
        super().__init__(file_path)

    def process_image(self):
        """
            Uploads given image to Gemini API as a JPEG

            Inputs:
                - N/A
            Outputs:
                - image file object
        """
        return genai.upload_file(self.file_path)

