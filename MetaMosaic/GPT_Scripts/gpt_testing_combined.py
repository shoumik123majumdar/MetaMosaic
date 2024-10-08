import os
import io
from google.cloud import vision
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import PyPDF2
from openai import OpenAI

# setup openai api key
openai_client = OpenAI(
    api_key=os.environ.get('API_KEY')
)

# setup google cloud vision api
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/rahuldmello/Desktop/Co-op/AI_testing/GPT4_testing/gpt-testing-431616-7a9b204deef1.json'
client = vision.ImageAnnotatorClient()

# setup azure computer vision api
subscription_key = os.environ.get('SUBSCRIPTION_KEY')
endpoint = 'https://gpt-testing.cognitiveservices.azure.com/'

# initialize computer vision api
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


def get_google_image_description(image_path):
    """
    Analyze the image and return a description using Google cloud vision

    :param image_path: Path to image file
    :return: Description of image
    """
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

        image = vision.Image(content=content)

        # perform label detection
        label_response = client.label_detection(image=image)
        labels = label_response.label_annotations
        label_descriptions = ', '.join(label.description for label in labels)

        # perform text detection
        text_response = client.text_detection(image=image)
        texts = text_response.text_annotations
        text_descriptions = ' '.join(text.description for text in texts)

        # perform object detection
        object_response = client.object_localization(image=image)
        objects = object_response.localized_object_annotations
        object_descriptions = ', '.join(object.name for object in objects)

        # perform web detection (to capture any relevant web entities)
        web_response = client.web_detection(image=image)
        web_entities = web_response.web_detection.web_entities
        web_descriptions = ', '.join(entity.description for entity in web_entities if entity.description)

        # combine and clean up descriptions
        combined_description = (
            f"Labels: {label_descriptions}. "
            f"Detected Text: {text_descriptions}. "
            f"Objects: {object_descriptions}. "
            f"Web Entities: {web_descriptions}."
        )

        # remove any redundant or empty descriptions
        combined_description = ". ".join(filter(None, combined_description.split('. ')))

        return combined_description


def get_azure_image_description(image_path):
    print("Starting image description extraction with Azure...")  # Debugging statement

    # Read the image into memory
    with open(image_path, "rb") as image_stream:
        # Use the Computer Vision API to analyze the image
        analysis = computervision_client.analyze_image_in_stream(image_stream, visual_features=[
            VisualFeatureTypes.description,  # Corrected feature
            VisualFeatureTypes.tags,
            VisualFeatureTypes.objects,
            VisualFeatureTypes.categories,
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


def generate_image_descriptions(combined_description, guidelines, back_combined_description=None):
    """
    Generate title, abstract, and subjects based on the image description and guidelines

    :param image_description: description of image as generated by Google Vision
    :param guidelines: guidelines for generating title and abstracts
    :return: Generated title, abstract, and subjects
    """

    if back_combined_description:
        combined_description = f'Front: {combined_description}. Back: {back_combined_description}'
    else:
        combined_description = f"Front: {combined_description}"

    response = openai_client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"You are an expert in library collections. Follow these guidelines strictly: {guidelines}"},
            {"role": "user", "content": f"Description: {combined_description}. Please provide a title, and abstract, and subjects (or keywords)."}
        ],
        model='gpt-4o-mini',
    )

    return response.choices[0].message.content


# paths
front_image_path = '/Users/rahuldmello/Desktop/Co-op/AI_testing/GPT4_testing/neu_m0449024q.jpg'
back_image_path = '/Users/rahuldmello/Desktop/Co-op/AI_testing/GPT4_testing/neu_m04490268.jpg'
pdf_path = '/Users/rahuldmello/Desktop/Co-op/AI_testing/GPT4_testing/Photograph_metadata_guidelines.pdf'

# extract front image description for both GV and Azure
google_description = get_google_image_description(front_image_path)
azure_description = get_azure_image_description(back_image_path)

# combine front descriptions
front_combined_descriptions = f"{google_description} {azure_description}"

# optionally extract and combine image descriptions for back of image
back_combined_description = None
if os.path.exists(back_image_path):
    back_google_description = get_google_image_description(back_image_path)
    back_azure_description = get_azure_image_description(back_image_path)
    back_combined_description = f"{back_google_description} {back_azure_description}"

# extract guidelines from pdf
guidelines = extract_text_from_pdf(pdf_path)

# generate title, abstract, and subjects
metadata = generate_image_descriptions(front_combined_descriptions, guidelines, back_combined_description)

print(f'Front Image Description: {front_combined_descriptions}')
if back_combined_description:
    print(f'Back Image Description: {back_combined_description}')
print(f'Generated Metadata: \n{metadata}')

