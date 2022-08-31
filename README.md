# Flask Container for Communicating with the Stability AI image generation API (DreamStudio)

* This app will generate an image based upon the prompt you provide it, and save that image to the static folder
* The prompt is accessed by the following url query
    * /prompt/?prompt=YOUR_PROMPT_HERE
* Images are stored locally in the /static/images/ directory
* Once the success response is returned, you can access the image via <img src"YOUR_URL_HERE/static/images/image.png">


* Please report any issues you have, and submit a pull request if you have a better way.

## To Get Started

* Install all dependencies for this project
    * pip install -r requirements.txt
* Open the 'main.py' file and input your API key
* You will need a server to host this, some options would be ngrok, Amazon ECS, or Amazon Lightsail(beginner-friendly)
