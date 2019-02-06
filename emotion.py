import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='2PbzMnZlhToXPujdP_LqXkHt9uKgSsJGZjhZ6JCGW4rU',
    url='https://gateway-lon.watsonplatform.net/tone-analyzer/api'
)

text = 'Team, I have alot of money'\
    'I am so happy'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
