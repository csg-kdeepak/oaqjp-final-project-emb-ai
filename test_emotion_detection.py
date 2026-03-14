from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    @staticmethod
    def get_highest_value_emotion(emotions):
        effective_emotion = None
        value = None
        for e, v in emotions.items():
            if effective_emotion is None or v > value:
                effective_emotion = e
                value = v
        return effective_emotion

    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")
        highest = self.get_highest_value_emotion(result1)
        print(highest)