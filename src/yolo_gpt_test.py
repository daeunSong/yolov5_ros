from openai import OpenAI
import requests

PAUSE = None

class GPT4vSocial:
    def __init__(self):
        rospy.Subscriber(rospy.get_param("~output_topic"), BoundingBoxes, self.callback, queue_size=10)

    def callback(self, msg):
        detections = msg.bounding_boxes
        for detection in detections:
            if detection.Class == "person" and detection.ymax - detection.ymin > 100:
                PAUSE = True
            else:
                PAUSE = False