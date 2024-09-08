from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    print(response)
    label = response['dominant_emotion']
    if label is None:
        return "Invalid text! Please try again!."
    else:
        score = response[label]
        return "The given text has been identified as {} with a score of {}.".format(label, score) 

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)