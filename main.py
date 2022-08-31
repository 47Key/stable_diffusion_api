from distutils.command import upload
from flask import *
import json, time
import warnings
import io
import os
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# SETTING API KEY WITH STABILITY CLIENT
stability_api = client.StabilityInference(
    key='YOUR_STABILITY-AI/DREAMSTUDIO_API-KEY_HERE', 
    verbose=True,
)

# INITIALIZING FLASK APP
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
uploads_path = os.path.join(basedir, 'static/images/' + 'image.png')

# INITIALIZING HOME ROUTE, ASKING FOR PROMPT
@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Please include prompt in query, as /prompt/?prompt=PROMPT_HERE', 'Timestamp': time.time() } # Test json dump that explains prompt usage if a developer comes across it
    json_dump= json.dumps(data_set)

    return json_dump


# INITIALIZING PROMPT ROUTE, TAKING PROMPT AND GENERATING IMAGE
@app.route('/prompt/', methods=['GET'])
def request_page():
    
    # Accepts user query through request args
    user_query = str(request.args.get('prompt')) 

    # Uses query in the prompt for stability image generation
    answers = stability_api.generate(
        prompt=f"{user_query}"
    )

    # Checks if the image passes the generation filters (to make sure nothing NSFW is sent to the user)
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again."
                )
            # Checks if the artifact is an acceptable image
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary)) # Encodes binary into base64 to pass to user
                img.save(uploads_path, "png") # saves image to image.png in static folder
                data_set = {'Page': 'Prompt', 'Image': 'Success', 'Location': '/static/images/image.png', 'Timestamp': time.time() } # Returns success when image is saved, allowing the url /images to be presented on screen
                json_dump = json.dumps(data_set)


    return json_dump
@app.route('/images', methods=['GET'])
def return_image():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')