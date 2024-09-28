import gradio as gr
from transformers import pipeline
import os

pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
def generate_caption(image):
    if image is None:
        return "Please upload an image first."
    
    try:
        result = pipe(image)
        return f"Image Description: {result[0]['generated_text']}"
    except Exception as e:
        return f"Error processing the image: {str(e)}"

def upload_image(image):
    if image is not None:
        return image, "Image uploaded. Click 'Generate Caption' to process."
    return None, "No image uploaded."

# Gradio
with gr.Blocks() as iface:
    gr.Markdown("# Image Captioning App")
    gr.Markdown("Upload an image and click 'Generate Caption' to get a description.")
    
    with gr.Row():
        image_input = gr.Image(type="pil", label="Upload Image")

    upload_button = gr.Button("Upload Image")
    status_text = gr.Textbox(label="Status", interactive=False)
    generate_button = gr.Button("Generate Caption")
    output_text = gr.Textbox(label="Generated Caption", interactive=False)
    upload_button.click(
        fn=upload_image,
        inputs=image_input,
        outputs=[image_input, status_text]
    )
    generate_button.click(
        fn=generate_caption,
        inputs=image_input,
        outputs=output_text
    )
# Launch the app
iface.launch()