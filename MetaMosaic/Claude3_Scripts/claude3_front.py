import base64
import os
import anthropic

# setup Claude 3 api key
api_key = os.environ.get('API_KEY')

def process_image_and_generate_metadata(image_path, title_prompt, abstract_prompt):
    """
    This function takes an image path, title prompt, and abstract prompt,
    then it returns the image description, title, and abstract.
    """
    # Encode image to base 64
    with open(image_path, 'rb') as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

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
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",  # You can change this if the image is in another format
                            "data": base64_image,
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
image_path = 'neu_230330.jpg'
title_prompt_path = '/Users/rahuldmello/Desktop/Co-op/AI_testing/Claude3_testing/title_prompt.txt'
abstract_prompt_path = '/Users/rahuldmello/Desktop/Co-op/AI_testing/Claude3_testing/abstract_prompt.txt'

# Load the prompts
title_prompt = load_prompt_from_file(title_prompt_path)
abstract_prompt = load_prompt_from_file(abstract_prompt_path)

# Process the image and generate the title and abstract
content, total_tokens = process_image_and_generate_metadata(image_path, title_prompt, abstract_prompt)

print(f'Generated Content: \n{content}')
print(f'Total Tokens Used: {total_tokens}')
