from abc import ABC, abstractmethod


class TranscriptionModel(ABC):
    """
    Interface for classes that handle transcribing text from the back of the image
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.transcription = self.generate_transcription(self.file_path)

    @abstractmethod
    def _generate_transcription(self):
        """
        Generates transcription from image at self.file_path
        Inputs:
            - None
        Outputs:
            - self.transcription is initialized
        """
        pass

    @abstractmethod
    def extract_names(self):
        """
        Extracts and returns the photographers name from the raw_transcription
        Inputs:
            - None
        Outputs:
            - Returns the photographer name as a string
        """
        pass

    @abstractmethod
    def extract_dates(self):
        """
        Extracts and returns a list of dates present in the raw_transcription
        Inputs:
            - None
        Outputs:
            - Returns list of dates
        """
        pass

    @abstractmethod
    def get_raw_transcription(self):
        """
        Gets the raw transcription that was initialized during object creation (self.transcription) and returns it
        Inputs:
            - None
        Outputs:
            - Returns self.transcription as the raw transcription
        """
        pass
