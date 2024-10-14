import unittest
from MetaMosaic.System_Design_Prototype.Image_Processors.gemini_image_processor  import GeminiImageProcessor


class TestGeminiImageProcessor(unittest.TestCase):

    def setUp(self):
        """Set up test resources (runs before each test case)"""
        self.file_path = "test_image.png"
        self.processor = GeminiImageProcessor(self.file_path)

    def test_process_image(self):
        """Test the image processing functionality."""
        self.processor.process_image()

    def test_process_image_fails(self):
        """Test that image processing functionality fails"""


if __name__ == '__main__':
    unittest.main()