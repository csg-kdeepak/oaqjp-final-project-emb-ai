from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, get_dominant_emotion

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    '''
        function to detect the emotion of the text provided
    '''
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse.strip():
        return "Please specify test to analyze."

    response = emotion_detector(text_to_analyse)

    if response is None:
        return "Couldn't detect the emotion. Please check the input text."
    
    dominant_emotion = get_dominant_emotion(response)

    return f"For the given statement, the system response is 'anger': {response['anger']}," + \
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy':" + \
        f" {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    '''
        rendering the index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)