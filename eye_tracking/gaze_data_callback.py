from eye_tracking.parser import Parser
from eye_tracking.local_storage import LocalStorage
from eye_tracking.config import EYE_TRACKING_DATA_FILENAME

global_gaze_data = {}

def gaze_data_callback(gaze_data, level_id) -> None:
    global global_gaze_data
    if level_id not in global_gaze_data:
        global_gaze_data[level_id] = []
    global_gaze_data[level_id].append(gaze_data)

def get_gaze_data(level_id):
    global global_gaze_data
    if level_id in global_gaze_data:
        return global_gaze_data[level_id]
    return []


