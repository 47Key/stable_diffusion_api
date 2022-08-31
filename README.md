# Flask Container for Communicating with the Stability AI image generation API (DreamStudio)

* This app will generate an image based upon the prompt you provide it, and save that image to the static folder
* The prompt is accessed by the following url query
    * /prompt/?prompt=YOUR_PROMPT_HERE
* Once the success response is returned, you can access the image via <img src"YOUR_URL_HERE/static/images/image.png">

## To get Started

* Install all depencies for this project
    * pip install stability-sdk
* Open the 'main.py' file and input your API key
* You will need a server like ngrok or Amazon ECS (ECS after the flask container is put into a docker image) to run this file, or you can use localhost for the time being
