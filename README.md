
# EchoPy
A python based Hello World demo Amazon Echo.

## Requirements and setup
EchoPy is built using python with flask. Amazon also requires that the server running the code be publicly accessible on port 443 using https. This means that you will either have to host it on a VPS or port forward 443 from your router. 

### Local development environment
Your computer or virtual environment needs the following installed before you go any further:

* Python
* [PIP](https://pip.pypa.io/en/stable/installing.html)

To run EchoPu, you'll need the python packages specified in [requirements.txt](./requirements.txt).

Once you have the above requirements installed on your computer, clone this repository, and run the following from the project root to get the environment setup for running EchoNestPy:

1. `pip install -r requirements.txt`


### Setting Up Server

The Alexa Skills Kit (ASK) requires that the server has an open connection to the internet on port 443 (HTTPS) with a SSL Certificate (self signed is okay). Right now this runs in flask with out HTTPS but I am looking into changing this. One way to work around this is to use STunnel4 or ngix forwarding to accept connections on 443 and connect to the app on port 5000. 

### Setting Up Alexa Skills Kit on Amazon

The ASK is available at: https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/getting-started-guide 

2. Sign in or Create an Account. 
2. Go to Apps & Services at the top of the page
2. Click on Alexa
2. Click Add New Skill
2. Fill out the first form:
** Name: Anything you want it to be - I use Nest Control
** Invocation Name: The hotword to call the app - I have gotten it working with Demo Hello
** Version: 1.0 <- This is hard-coded for now
** Endpoint: https://<domain or ip address\>/alexa/EchoPyAPI
2. Go to the next page and copy the intentSchema.json to the Intent Schema and sampleUtterances.txt to the Sample Utterances
2. Go to the next page and upload the self signed SSL Cert you have.. and hit next..

## Usage
````
run: python echopy.py
````

At this time you will have to go to your Echo and say 'Alexa, Talk to Demo Hello' (Replace Nest with what the Invocation Name you set).


