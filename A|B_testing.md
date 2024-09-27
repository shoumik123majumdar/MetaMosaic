# A|B testing for Claude and Gemini Prototypes
[Link to Labeled Images in DRS] () 
### Claude vs Gemini vs Labeled Images

## Development
100 images for Test 1 (to help development)  
100 images for Test 2 (for a final set)  

To source the images, choose between either pulling from the **DRS API** or **Discovery Cluster**  

### **DRS API**  
#### Pros  
  - Experience Implementing a data pipeline like this before
#### Cons  
  - Images may not be uploaded to the DRS


### **Discovery Cluster**  
#### Pros  
  - All images that are digitized should be stored here  
  - Probably more efficient method (will test)  
#### Cons  
  - Not sure how difficult it is to develop the pipeline  
  - For dev-time purposes, could be less efficient if we want this done ASAP  

### CSV File Requirements
  - Image Title
  - Title
  - Abstract
  - Photographer Name (if it exists)
  - Dates (if it exists)
Once each of the 200 images are processed (using pandas --> csv files --> excel) we can move onto A|B testing

## A|B testing
5 images for comparison testing
Rank based from 1-4 (Gemini vs. Claude Opus vs. Claude Sonnet vs. Human Generated)

4 images for metric testing
- Accuracy
- Conciseness
Presentation: Get Feedback from Audience from a Demo.
