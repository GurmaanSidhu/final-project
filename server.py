"""
Flask server for Emotion Detection application.
This module provides web routes to analyze user input text
and display emotion detection results using the
EmotionDetection package.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def home():
    """
    This part render's the home page on the web.
    The main UI where a person lands at first.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Analyze text provided by the user and return emotion results.
    this part returns -A formatted string containing emotion scores and
        the dominant emotion, or an error message for invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
