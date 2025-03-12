"""
This file is the server file for an Emotion Detector web application. It uses Flask to 
handle web requests and the emotion_detector function from the EmotionDetection package 
to analyze the emotions in a text message.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotions in the text and returns the emotion scores and 
    the dominant emotion.

    This function retrieves the text to analyze from the request, passes it to the
    emotion_detector function, and returns the emotion scores and dominant emotion.
    If no dominant emotion is found, an error message is returned.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant emotion is None (indicating an error or invalid input)
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    # Return a formatted string with the emotion scores and dominant emotion
    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': "
            f"{sadness}. The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """
    Renders the index page for the web application.
    
    This function simply returns the HTML file (index.html) that contains the
    interface for the user to input text for emotion detection.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)
