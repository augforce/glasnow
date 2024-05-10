import urllib.request\
import json\
import os\
import ssl\
\
def allowSelfSignedHttps(allowed):\
    # bypass the server certificate verification on client side\
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):\
        ssl._create_default_https_context = ssl._create_unverified_context\
\
allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.\
\
# Request data goes here\
# The example below assumes JSON formatting which may be updated\
# depending on the format your endpoint expects.\
# More information can be found here:\
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script\
data =  \{\
  "Inputs": \{\
    "input1": [\
      \{\
        "Pitch": "4-Seam Fastball",\
        "L/R": "L",\
        "Balls": 2,\
        "Strikes": 0,\
        "Runner on 3B": false,\
        "Runner on 2B": false,\
        "Runner on 1B": false,\
        "Outs": 2\
      \},\
      \{\
        "Pitch": "4-Seam Fastball",\
        "L/R": "L",\
        "Balls": 1,\
        "Strikes": 0,\
        "Runner on 3B": false,\
        "Runner on 2B": false,\
        "Runner on 1B": false,\
        "Outs": 2\
      \},\
      \{\
        "Pitch": "4-Seam Fastball",\
        "L/R": "L",\
        "Balls": 0,\
        "Strikes": 0,\
        "Runner on 3B": false,\
        "Runner on 2B": false,\
        "Runner on 1B": false,\
        "Outs": 2\
      \},\
      \{\
        "Pitch": "Slider",\
        "L/R": "R",\
        "Balls": 0,\
        "Strikes": 2,\
        "Runner on 3B": true,\
        "Runner on 2B": false,\
        "Runner on 1B": false,\
        "Outs": 1\
      \},\
      \{\
        "Pitch": "Slider",\
        "L/R": "R",\
        "Balls": 0,\
        "Strikes": 1,\
        "Runner on 3B": true,\
        "Runner on 2B": false,\
        "Runner on 1B": false,\
        "Outs": 1\
      \}\
    ]\
  \},\
  "GlobalParameters": \{\}\
\}\
\
body = str.encode(json.dumps(data))\
\
url = 'http://172.168.144.124:80/api/v1/service/glasnowendpoint/score'\
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint\
api_key = ''\
if not api_key:\
    raise Exception("A key should be provided to invoke the endpoint")\
\
\
headers = \{'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)\}\
\
req = urllib.request.Request(url, body, headers)\
\
try:\
    response = urllib.request.urlopen(req)\
\
    result = response.read()\
    print(result)\
except urllib.error.HTTPError as error:\
    print("The request failed with status code: " + str(error.code))\
\
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure\
    print(error.info())\
    print(error.read().decode("utf8", 'ignore'))}
