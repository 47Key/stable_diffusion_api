from flask import *
import json, time
import warnings
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from base64 import b64encode

# SETTING API KEY WITH STABILITY CLIENT
stability_api = client.StabilityInference(
    key='ENTER_YOUR_STABILITY/DREAMSTUDIO_API_KEY_HERE', 
    verbose=True,
)

# INITIALIZING FLASK APP
app = Flask(__name__)

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
                img = b64encode(artifact.binary) # Encodes binary into base64 to pass to user
                data_set = {'Page': 'Prompt', 'Image': f'{img}', 'Timestamp': time.time() } # Includes the base 64 encoded image in JSON
                json_dump = json.dumps(data_set)


    return json_dump

if __name__ == '__main__':
    app.run(host='0.0.0.0')