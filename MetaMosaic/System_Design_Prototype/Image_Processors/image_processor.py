from abc import ABC, abstractmethod


class ImageProcessor(ABC):
    """
    Interface for classes that handle image pre-processing before feeding images into an AI model
    """
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def process_image(self):
        """
            Takes file at self.file_path and stores it within new_location for use within the data pipeline
            Depending on the AI Model being used, necessary pre_processing for the image will be applied before image is stored
            Ie: encoded into base_64 for Anthropic models.
            Inputs:
                - None
            Outputs:
                - None
        """
        pass

    """
    """
    def resize(self):
        pass


