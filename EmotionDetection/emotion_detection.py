import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the text for emotions using the Watson NLP Library,
    extracts specific emotion scores, and identifies the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API
    response = requests.post(url, json=input_json, headers=header)
    
    # Convert the response text into a dictionary using the json library
    formatted_response = json.loads(response.text)
    
    # Extract emotions and scores from the response structure
    # (Depending on the exact API response layout, scores are typically under emotion predictions)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions.get('anger', 0.0)
    disgust_score = emotions.get('disgust', 0.0)
    fear_score = emotions.get('fear', 0.0)
    joy_score = emotions.get('joy', 0.0)
    sadness_score = emotions.get('sadness', 0.0)
    
    # Create a dictionary of the extracted emotions
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Find the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Add the dominant emotion to the return dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    return emotion_scores