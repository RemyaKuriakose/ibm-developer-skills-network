from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the text passed via query parameters and returns 
    the formatted emotion detection results.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)
    
    # Optional edge-case handling for blank/invalid text inputs
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    # Extract individual emotion scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Return the exact formatted response string required
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} "
        f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application web interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application locally on port 5000
    app.run(host="0.0.0.0", port=5000)