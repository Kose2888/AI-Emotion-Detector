import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    #print(f"DEBUG: {formatted_response}")

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Find the value with the highest score
        highest_score = max(emotions, key=emotions.get)
        # Get the key with the highest score = the dominant emotion
        highest_emotion = emotions[highest_score]

        # Add the dominant emotion to the dict
        emotions["dominant_emotion"] = highest_score 
        
    elif response.status_code == 400:
        emotions = None

    elif response.status_code == 500:
        emotions = None

    return emotions
