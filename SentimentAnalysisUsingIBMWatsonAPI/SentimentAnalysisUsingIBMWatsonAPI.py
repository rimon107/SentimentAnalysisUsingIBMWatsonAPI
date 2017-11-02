import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="XXXXXXXX",
  password="XXXXXXXX",
  version="2017-02-27",
  url = 'https://gateway-fra.watsonplatform.net/natural-language-understanding/api')

response = natural_language_understanding.analyze(
  text="The problem of sarcasm comes when you employ 'Bag of Words' approach",
  features=[
    Features.Sentiment()
  ]
)

print(json.dumps(response, indent=2))
