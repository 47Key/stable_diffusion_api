# Flask Container for Communicating with the Stability AI image generation API (DreamStudio)

* This app will generate an image based upon the prompt you provide it, and return a JSON object with a base64 encoded image, meant to be queried as an API
* The prompt is accessed by the following url query
    * /prompt/?prompt=YOUR_PROMPT_HERE
* In theory the returned Image can be used in a html image tag, like this: <img src=`data:image/png;base64, ${json.image}` />
* There is a pre-configured dockerfile in this repository, that is ready to be built and deployed if that is a better option for you, the repository is "https://github.com/47Key/stable-diffusion_api-docker"

* Please report any issues you have, and submit a pull request if you have a better way.

## To Get Started

* Install all dependencies for this project
    * pip install -r requirements.txt
* Open the 'main.py' file and input your API key
* You will need a server to host this, some options would be ngrok, Amazon ECS, or Amazon Lightsail(beginner-friendly)
