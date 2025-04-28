from ollama import chat
from ollama import Client

import yaml
import json

with open('settings.yml', 'r') as f:
    settings = yaml.load(f, Loader=yaml.SafeLoader)

ai_settings = settings.get('OllamaAI')  

imagePath = ai_settings['ai_imagepath']
client = Client(
    host = ai_settings['ai_host']
)

prompt = 'What plant is this? Is it Healthy? If its not healthy what are the issues? Whats the description of the plant? Answer in json format'

def OllamaApiRequest():

    with open(imagePath, 'rb') as image_file:
        image = image_file.read()
    
    response = client.chat(
        model='gemma3:12b',
        options={'temperature': 0}, 
        messages=[
            {
                'role': 'user',
                'content': '''What plant is this? Is it Healthy? If its not healthy what are the issues? Whats the description of the plant? Provide clear prediction of the issues of the plant'
                strictly use the following json format:
                {
                    "Name": "",
                    "Condition": "",
                    "Issues": {
                        
                    },
                    "Recommendations": {
                        "Pest Management": "",
                        "Nutrient Supplementation": "",
                        "Pruning and Training": "",
                        "Disease Prevention and Treatment": ""
                    }
                }
                
                Do not use any formatting in the response''',
                'images': [image],
            }
        ],
    )
    print(response['message']['content'])
    

    

OllamaApiRequest()

