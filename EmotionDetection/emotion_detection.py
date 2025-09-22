import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    formatted_response = json.loads(response.text)
    emotion = ""
    temp = 0
    count = 0
    vals = formatted_response['emotionPredictions'][0]['emotion']
    for resp in vals:
        chk = vals[resp]
        if count == 0:
            temp = chk
            emotion = resp
        else:
            if chk > temp:
                temp = chk
                emotion = resp
        count +=1
    vals["dominant_emotion"] = emotion
    return vals


    """
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I love this new technology.")

    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    return {'label': label, 'score': score}
    """