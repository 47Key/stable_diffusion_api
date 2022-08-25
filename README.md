# Flask Container for Communicating with the Stability AI image generation API (DreamStudio)

* This app will generate an image based upon the prompt you provide it, and return a JSON object with a base64 encoded image, meant to be queried as an API

## To get Started

* Install all depencies for this project
    - pip install stability-sdk
* Open the 'main.py' file and input your API key
* You will need a server like ngrok or Amazon ECS (ECS after the flask container is put into a docker image) to run this file, or you can use localhost for the time being
# stable_diffusion_api
