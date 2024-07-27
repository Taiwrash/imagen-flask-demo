import argparse

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        # Call your backend function to generate the image based on the prompt
        image_path = generate_image(
            project_id='qwiklabs-gcp-03-554bf2cf3317',
            location='us-east4',
            output_file='static/images/image.jpeg',
            prompt=prompt,
            )
        return render_template('index.html', prompt=prompt, image_generated=True, image_path=image_path)
    return render_template('index.html', image_generated=False)

def generate_image(
    project_id: str, location: str, output_file: str, prompt: str
) -> vertexai.preview.vision_models.ImageGenerationResponse:
    """Generate an image using a text prompt.
    Args:
      project_id: Google Cloud project ID, used to initialize Vertex AI.
      location: Google Cloud region, used to initialize Vertex AI.
      output_file: Local path to the output image file.
      prompt: The text prompt describing what you want to see."""

    vertexai.init(project=project_id, location=location)

    model = ImageGenerationModel.from_pretrained("imagegeneration@002")

    images = model.generate_images(
        prompt=prompt,
        # Optional parameters
        number_of_images=1,
        seed=1,
        add_watermark=False,
    )

    images[0].save(location=output_file)

    return images

@app.route('/api/generate', methods=['POST'])
def api_generate_image():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    # Call your backend function to generate the image based on the prompt
    image_path = generate_image(
                    project_id='qwiklabs-gcp-03-554bf2cf3317',
                    location='us-east4',
                    output_file='image.jpeg',
                    prompt=prompt
                )
    
    # Return the path to the generated image
    return jsonify({'message': "successfully created"})

if __name__ == '__main__':
    app.run(debug=True)
