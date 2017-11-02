# SentimentAnalysisUsingIBMWatsonAPI
Python version: 3.5.2

Install python package:

pip install watson_developer_cloud

First create account in blumix.net and then add Natural Language Understanding API to service. 
from the service credential, get username and password.


Output:
{
  "usage": {
    "text_units": 1,
    "text_characters": 4007,
    "features": 1
  },
  "sentiment": {
    "document": {
      "score": -0.74758,
      "label": "negative"
    }
  },
  "language": "en"
}

link of example text : https://natural-language-understanding-demo.mybluemix.net/

