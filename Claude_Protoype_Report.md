# Claude Report

## Prompts:
#### Abstract Prompt:
You are an expert in digital library collections. Follow these guidelines strictly
ADHERE to these general rules for an abstract:
A brief objective summary (2-5 SENTENCES) of the content, meaning, subject matter or composition of the image, if not apparent from the title (there is additional information to provide).
INCLUDE, if context is provided: date or date span depicted;
INCLUDE a description of the composition of the image; the most significant topic(s), event(s), person(s), place(s), etc.

Output Formatting:
Abstract: abstract

Please generate an abstract based on the given general rules
Also provided could potentially (if after the : it is not blank) be context from the back of the given photo, which SHOULD BE USED to formulate a more descriptive/accurate abstracts:


#### Title Prompt:
You are an expert in digital library collections. Follow these guidelines strictly
Please generate a title for the given image based on these rules:
Title should be ~MUST BE 20 WORDS OR LESS.
For images of a documentary nature, give the objective factual content clearly and concisely.
MAKE SURE TO INCLUDE Succinct descriptive phrasing of the form or genre of the image from the following list:
- portrait
- map
- candid photograph
- landscape
- aerial photograph
- documentary photograph
- fashion photograph
- panoramic photograph
- sports action photograph
- street photograph
- illustration
- architectural photograph
INCLUDE an identification of the main subject(s) depicted (i.e., persons, events, activities, and objects)
ONLY INCLUDE race/ethnicity if it is absolutely necessary to the context of the image
DON'T Identify individuals by name, UNLESS NAMES ARE SPECIFIED IN GIVEN CONTEXT
INCLUDE the geographical and/or type of location depicted, if known and significant
Do NOT include: dates or a chronological descriptor

Output Formatting:
Title: generated title

Also potentially provided IN THIS PROMPT (if after the : it is not blank), is context from the back of the given photo,
WHICH SHOULD BE USED to formulate a more descriptive/accurate title:

#### Transcription Prompt:
Transcribe what's on this photo

Transcription rules
In general, use modern spacing conventions when transcribing from the source. Make no attempt to preserve additional or irregular spacing between words. If spacing between words in the source is ambiguous, or lacking, include spaces in the transcription to separate the words as needed.
Indicate missing letters in words with a “-“
Indicate single or multi-word omissions in the transcription by using “…”. When using the mark of omission, generally use it with a space on either side
Transcribe initials, initialisms, monograms, and acronyms without internal spaces (acronyms without periods), regardless of how they are presented in the source of information.
Transcribe an unintentional inaccuracy, misspelling, or misprint as it appears on the material. Follow such an inaccuracy either by “[sic]” or by the abbreviation “i.e.” and the correction within square brackets.

If you can, provide this information
- Name of Photographer
- Date(s) (Seperately if there are multiple)
- Any other text on the image.

Format the output like this text:
Name:Name of Photographer
Date:[Date1, Date2,...] (formatted as a list from earliest to latest date)
Raw:(Full raw transcription given the transcription rules above)


## Haiku
### Case 1: (Front Image Only)(673 Tokens)
Handle: http://hdl.handle.net/2047/d20156635 

Title: Four Smiling Women Portrait in Professional Attire
Abstract: This black-and-white documentary photograph depicts four women standing together, engaged in friendly conversation. The women are dressed in professional attire, suggesting a formal or business setting. Their smiles and body language indicate a positive, collaborative atmosphere. The image provides a glimpse into the social and professional interactions of women during this historical period, though the specific identities of the individuals are not provided.

Conclusions:
- 


### Case 2 (Front and Back)(1054 Tokens)
Handle: https://repository.library.northeastern.edu/files/neu:4f23c857b

Title: Documentary Photograph of Military Personnel Assembled on Airfield
Abstract: This documentary photograph depicts a large assembly of military personnel standing in orderly rows on an airfield. The men appear to be members of the armed forces, based on their uniforms and formation. The image captures a formal military gathering or inspection, with the individuals standing at attention and facing a central direction. The setting is outdoors, with a body of water and industrial structures visible in the background, suggesting the location may be a naval or military installation.

Conclusions:
- 


## Sonnet
### Case 1: (Front Image Only)(673 Tokens)
Handle: http://hdl.handle.net/2047/d20156635 

Title: Four Smiling Women Portrait in Professional Attire
Abstract: This black-and-white documentary photograph depicts four women standing together, engaged in friendly conversation. The women are dressed in professional attire, suggesting a formal or business setting. Their smiles and body language indicate a positive, collaborative atmosphere. The image provides a glimpse into the social and professional interactions of women during this historical period, though the specific identities of the individuals are not provided.

Conclusions:
- 


### Case 2 (Front and Back)(1054 Tokens)
Handle: https://repository.library.northeastern.edu/files/neu:4f23c857b

Title: Documentary Photograph of Military Personnel Assembled on Airfield
Abstract: This documentary photograph depicts a large assembly of military personnel standing in orderly rows on an airfield. The men appear to be members of the armed forces, based on their uniforms and formation. The image captures a formal military gathering or inspection, with the individuals standing at attention and facing a central direction. The setting is outdoors, with a body of water and industrial structures visible in the background, suggesting the location may be a naval or military installation.

Conclusions:
- 

## Opus
### Case 1: (Front Image Only)(673 Tokens)
Handle: http://hdl.handle.net/2047/d20156635 

Title: Four Smiling Women Portrait in Professional Attire
Abstract: This black-and-white documentary photograph depicts four women standing together, engaged in friendly conversation. The women are dressed in professional attire, suggesting a formal or business setting. Their smiles and body language indicate a positive, collaborative atmosphere. The image provides a glimpse into the social and professional interactions of women during this historical period, though the specific identities of the individuals are not provided.

Conclusions:
- 


### Case 2 (Front and Back)(1054 Tokens)
Handle: https://repository.library.northeastern.edu/files/neu:4f23c857b

Title: Documentary Photograph of Military Personnel Assembled on Airfield
Abstract: This documentary photograph depicts a large assembly of military personnel standing in orderly rows on an airfield. The men appear to be members of the armed forces, based on their uniforms and formation. The image captures a formal military gathering or inspection, with the individuals standing at attention and facing a central direction. The setting is outdoors, with a body of water and industrial structures visible in the background, suggesting the location may be a naval or military installation.

Conclusions:
- 

## Final Token Analysis
### Haiku
### Sonnet
**Average Input Tokens (Just Front): 1200**  
**Average Output Tokens (Just Front): 130**

Based on that...
- For every **50k** images processed: **$179 dollars** (input)
- For every **50k** images processed: **97 dollars** (output)
- **Total: 179 + 97 = $276**

### Opus

##Final Time Complexity
