"""
This is a server to respond the Emotion Detection of a phrase
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Emotion Detector will take a string and use the watson AI to
    Determine the emotion behind it. 
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear =  response['fear']
    joy = response['joy']
    sadness = response['sadness']
    em = response['dominant_emotion']


    # Check if the label is None, indicating an error or invalid input
    if em is None:
        message =  "Invalid text! Please try again!"
    else:
        message =  f"""For the given statement, the system response is 'anger': {anger},
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.
    The dominant emotion is {em}.
    """
    return message
@app.route("/")
def render_index_page():
    """
    Renders the index page
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
