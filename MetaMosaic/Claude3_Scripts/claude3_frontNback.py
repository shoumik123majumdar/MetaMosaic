import base64
import os
import anthropic

# setup Claude 3 api key
api_key = os.environ.get('API_KEY')


def encode_image(image_path):
    # Encode image to base 64
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def process_image_and_generate_metadata(front_image_path, back_image_path, title_prompt, abstract_prompt):
    """
    This function takes an image path, title prompt, and abstract prompt,
    then it returns the image description, title, and abstract.
    """
    # Encode front and back images to base 64
    front_image_base64 = encode_image(front_image_path)
    back_image_base64 = encode_image(back_image_path)

    # Claude API request
    client = anthropic.Anthropic(api_key=api_key)

    # Create a combined prompt to describe the image, and generate title and abstract
    response = client.messages.create(
        model='claude-3-opus-20240229',
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Front Image:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",  # You can change this if the image is in another format
                            "data": front_image_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Back Image:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",  # You can change this if the image is in another format
                            "data": back_image_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text": (
                            f"Generate a title based on the following title guidelines: {title_prompt}\n"
                            f"Now generate an abstract based on the following abstract guidelines: {abstract_prompt}"
                        )
                    }
                ]
            }
        ],
    )

    # Extract the content from the response
    content = response.content  # Access the response content
    usage = response.usage.input_tokens  # Access token usage

    return content, usage


def load_prompt_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()


# Paths to image and prompts
front_image_path = 'neu_4f1985390.jpg'
back_image_path = 'neu_4f1985411.jpg'
title_prompt_path = '../abstract_prompt.txt'
abstract_prompt_path = '../abstract_prompt.txt'

# Load the prompts
title_prompt = load_prompt_from_file(title_prompt_path)
abstract_prompt = load_prompt_from_file(abstract_prompt_path)

# Process the image and generate the title and abstract
content, total_tokens = process_image_and_generate_metadata(front_image_path, back_image_path, title_prompt, abstract_prompt)

print(f'Generated Content: \n{content}')
print(f'Total Tokens Used: {total_tokens}')
