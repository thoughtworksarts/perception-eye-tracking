from eye_tracking.parser import Parser
from eye_tracking.local_storage import LocalStorage


def gaze_data_callback(gaze_data):
    parser = Parser()
    left_eye_coordinates = parser.parse(gaze_data.left_eye)
    right_eye_coordinates = parser.parse(gaze_data.right_eye)

    local_storage = LocalStorage()
    local_storage.store(left_eye_coordinates, right_eye_coordinates)