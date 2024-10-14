from image_processor import ImageProcessor
import base64


class ClaudeImageProcessor(ImageProcessor):
    """
    Class Implementation of ImageProcessor interface for use with Claude Models
    """
    def __init__(self, file_path):
        super().__init__(file_path)

    def process_image(self):
        """
            Processes given image at self.file_path and converts it to base_64 encoding for use with Anthropic's Claude API
            Inputs:
                - None
            Outputs:
                - base_64 encoding of given image
        """
        with open(self.file_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')