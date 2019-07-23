from eye_tracking.parser import Parser
from eye_tracking.local_storage import LocalStorage
from eye_tracking.config import EYE_TRACKING_DATA_FILENAME


def gaze_data_callback(gaze_data) -> None:
    parser = Parser()
    left_eye_coordinates = parser.get_coordinates_from_eye_data(gaze_data.left_eye)
    right_eye_coordinates = parser.get_coordinates_from_eye_data(gaze_data.right_eye)
    local_storage = LocalStorage(file_name=EYE_TRACKING_DATA_FILENAME, mode='a+')
    local_storage.store(left_eye_coordinates, right_eye_coordinates)
    local_storage.close()
