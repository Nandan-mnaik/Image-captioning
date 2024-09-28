from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os
# Load the BLIP model and processor
try:
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
except Exception as e:
    print(f"Error loading the model: {str(e)}")
    exit(1)
# Function to generate caption for an image
def generate_caption(image_path, max_length=30, num_beams=5):
    # Check if file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")
    try:
        # Load the image
        image = Image.open(image_path).convert('RGB')
    except Exception as e:
        raise IOError(f"Error opening the image: {str(e)}")
    # Prepare the image for the model
    inputs = processor(images=image, return_tensors="pt")
    # Output
    output = model.generate(**inputs, max_length=max_length, num_beams=num_beams)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption
# Example usage
image_path = "C:/Users/Admin/Desktop/image-text/WIN_20240928_20_12_59_Pro.jpg"
try:
    caption = generate_caption(image_path, max_length=100, num_beams=7)
    print(f"Generated caption: {caption}")
except Exception as e:
    print(f"An error occurred: {str(e)}")