"""
This module deploys the web server.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Renders the index page for the root GET request"""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_analyser():
    """returns all emotion key-value pairs and the dominant emotion as a string"""
    text_to_analyse = request.args.get('textToAnalyze')

    emotion = emotion_detector(text_to_analyse)

    # Handle blank entries
    if emotion is None:
        return "Invalid text! Please try again!"

    first_four_emotions = dict(list(emotion.items())[:4])
    # Cast to string and remove the outside brackets
    first_four_emotions_string = str(first_four_emotions)[1:-1]

    fifth_emotion = dict(list(emotion.items())[4:5])
    fifth_emotion_string = str(fifth_emotion)[1:-1]

    dominant_emotion = emotion['dominant_emotion']

    formatted_response = f"""{first_four_emotions_string} and {fifth_emotion_string}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
