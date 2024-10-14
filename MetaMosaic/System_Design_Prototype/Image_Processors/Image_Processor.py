from abc import ABC, abstractmethod


"""
Interface for classes that handle image pre-processing before feeding images into an AI model
"""
class Image_Processor(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    """
    Depending on the AI Model being used, necessary pre_processing for the image will be applied before image is stored
    Ie: encoded into base_64 for Anthropic models. 
    Inputs:
        - N/A
    Outputs:
        - N/A
    """
    @abstractmethod
    def process_image(self):
        pass

    """
    Takes file at self.file_path and stores it within Image_Folder for use within the data pipeline
    """
    @abstractmethod
    def save_image(self):
        pass
