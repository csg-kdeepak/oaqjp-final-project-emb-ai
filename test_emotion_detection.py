from EmotionDetection.emotion_detection import emotion_detector, get_dominant_emotion
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_analyzer(self):
        result1 = emotion_detector("I am glad this happened")
        detected_emotion1 = get_dominant_emotion(result1)
        self.assertEqual(detected_emotion1, 'joy')

        result1 = emotion_detector("I am really mad about this")
        detected_emotion1 = get_dominant_emotion(result1)
        self.assertEqual(detected_emotion1, 'anger')

        result1 = emotion_detector("I feel disgusted just hearing about this")
        detected_emotion1 = get_dominant_emotion(result1)
        self.assertEqual(detected_emotion1, 'disgust')

        result1 = emotion_detector("I am so sad about this")
        detected_emotion1 = get_dominant_emotion(result1)
        self.assertEqual(detected_emotion1, 'sadness')

        result1 = emotion_detector("I am really afraid that this will happen")
        detected_emotion1 = get_dominant_emotion(result1)
        self.assertEqual(detected_emotion1, 'fear')

unittest.main()