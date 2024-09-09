import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import io
import PyPDF2
from openai import OpenAI

# setup openai api key
openai_client = OpenAI(
    api_key='sk-DaQ7ivxveeVp9VHjbn4CxhN4xLtB8PnO-NM5fGIIQjT3BlbkFJ4aFykXZzJuh38UiwlUdtJbasG5lw_-UhupTWzNfy0A'
)

# setup azure computer vision api
subscription_key = 'c55fa775b69148f1bf87312c7b9088bf'
endpoint = 'https://gpt-testing.cognitiveservices.azure.com/'

# initialize computer vision api
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def get_image_description(image_path):
    print("Starting image description extraction with Azure...")  # Debugging statement

    # Read the image into memory
    with open(image_path, "rb") as image_stream:
        # Use the Computer Vision API to analyze the image
        analysis = computervision_client.analyze_image(image_stream, visual_features=[
            VisualFeatureTypes.DESCRIPTION,  # Corrected feature
            VisualFeatureTypes.TAGS,
            VisualFeatureTypes.OBJECTS,
            VisualFeatureTypes.CATEGORIES,
        ])

    # Extract the description from the analysis
    description = analysis.description.captions[0].text if analysis.description.captions else "No description available"
    tags = ', '.join(tag.name for tag in analysis.tags) if analysis.tags else "No tags available"
    objects = ', '.join(obj.object_property for obj in analysis.objects) if analysis.objects else "No objects detected"
    categories = ', '.join(
        cat.name for cat in analysis.categories) if analysis.categories else "No categories available"

    # Combine and clean up descriptions
    combined_description = (
        f"Description: {description}. "
        f"Tags: {tags}. "
        f"Objects: {objects}. "
        f"Categories: {categories}."
    )

    print("Combined image description from Azure:", combined_description)  # Debugging statement
    return combined_description


def extract_text_from_pdf(pdf_path):
    """
    Extract text from pdf file
    :param pdf_path: path to pdf file
    :return: extracted text
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    return text


def generate_image_descriptions(image_description, guidelines):
    print("Starting metadata generation...")  # Debugging statement

    chat_completion = openai_client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"You are an expert in library collections. Follow these guidelines strictly: {guidelines}"},
            {"role": "user", "content": f"Description: {image_description}. Please provide a title, an abstract, and subjects (or keywords)."}
        ],
        model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
    )

    print("Metadata generated.")  # Debugging statement
    return chat_completion.choices[0].message.content


# paths
image_path = '/Users/rahuldmello/Desktop/Co-op/AI_testing/GPT4_testing/neu_126321.jpg'
pdf_path = '/Users/rahuldmello/Desktop/Co-op/AI_testing/GPT4_testing/Photograph_metadata_guidelines.pdf'

# extract image description
image_description = get_image_description(image_path)

# extract guidelines from pdf
guidelines = extract_text_from_pdf(pdf_path)

# generate title, abstract, and subjects
metadata = generate_image_descriptions(image_description, guidelines)

print(f'Image Description: {image_description}')
print(f'Generated Metadata: \n{metadata}')
