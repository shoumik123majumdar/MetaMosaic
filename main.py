import google.generativeai as genai
import os
import PIL.Image
import re
import time

GOOG_KEY = os.environ.get("GOOG_KEY")

genai.configure(api_key = GOOG_KEY)
generation_config= genai.GenerationConfig(temperature=0)
model = genai.GenerativeModel("gemini-1.5-pro",generation_config=generation_config)

img_file_path = "Boston_Globe_Imgs"
image_front = "Test_15.tif"
image_back = "Test_15Back.tif"

"""
Processes a given image (if tif formatted, converts it to jpg), and returns it as an JPEG that has slightly reduced quality.
Inputs:
    - file_path: name of the folder where the tif_img resides, as well as where you want the images to be saved
    - tif_img: name of the individual tif file to be processed
Outputs:
    - img: variable that holds the processed image ready to be inputted into the model
"""
def process_image(file_path,tif_img):
    with PIL.Image.open(f"{file_path}/{tif_img}") as img:
        img.save(f"{file_path}/Test.jpeg", 'JPEG', quality=85)
    return img


#Process the back of the photo
img = process_image("Boston_Globe_Imgs",image_back)

prompt = ""
with open("transcription_prompt.txt","r") as file:
    prompt = file.read()

response = model.generate_content(contents=[prompt,img])
transcription = response.text
print(response)



"""
Extracts the photographer name , dates and the raw transcription from the given text 
Inputs:
    - text: text from the transcribed back
Outputs:
    - name: photographer name
    - dates: date(s) 
    - raw_text: raw transcription
"""
def extract_details(text):

    name_match = re.search(r'Name:(.*)', text)
    name = name_match.group(1).strip() if name_match else None


    dates_match = re.search(r'Date:\[(.*?)\]', text)
    dates = dates_match.group(1).split(', ') if dates_match else []

    raw_match = re.search(r'Raw:(.*)', text, re.DOTALL)
    raw_text = raw_match.group(1).strip() if raw_match else None

    return name, dates, raw_text

#Find a database - MongoDB + SQL
name, dates, raw_text = extract_details(transcription)
print("Name: " + name)
print("Dates: " + str(dates))
print("Raw: " + raw_text)
time.sleep(4) #To mitigate concurrent request issues


img = process_image(img_file_path,image_front)

with open("title_prompt.txt","r") as file:
    prompt = file.read()

title_prompt = prompt + raw_text


response = model.generate_content(contents=[title_prompt,img])
title = response.text #Generated title
print(title)
print(response)
time.sleep(4)

#Generate the abstract
with open("abstract_prompt.txt","r") as file:  # Load up the prompt from the abstract_prompt.txt file
    prompt = file.read()

#Add raw context to the general prompt
abstract_prompt = prompt + raw_text

#Generate the abstract
response = model.generate_content(contents=[abstract_prompt,img])
print(response)
print(response.text)

"""
#Spreadsheet + Cost Benefit
"""