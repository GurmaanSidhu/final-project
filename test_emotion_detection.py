from EmotionDetection import emotion_detector

def test_emotion_detection():
    assert emotion_detector("I am glad this happened")["dominant_emotion"] == "joy"
    assert emotion_detector("I am really mad about this")["dominant_emotion"] == "anger"
    assert emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"] == "disgust"
    assert emotion_detector("I am so sad about this")["dominant_emotion"] == "sadness"
    assert emotion_detector("I am really afraid that this will happen")["dominant_emotion"] == "fear"

    print("All emotion detection tests passed!")

if __name__ == "__main__":
    test_emotion_detection()
