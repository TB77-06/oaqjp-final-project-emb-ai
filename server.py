"""
This module provides functionalities for emotion detection using Flask.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to analyze the user-provided text for emotions and return the result.

    This function retrieves the text to be analyzed from the request arguments,
    passes it to the emotion_detector function, and returns the detected emotion
    scores and the dominant emotion as a formatted string.

    Returns:
        str: A formatted string containing the emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid input! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {response['anger']} "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
        )

@app.route("/")
def render_index_page():
    """
    Render the main application page.

    This function renders the index.html template when the root URL is accessed.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
