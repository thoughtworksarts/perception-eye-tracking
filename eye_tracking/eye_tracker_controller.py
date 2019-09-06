from tobiiresearch.implementation.EyeTracker import EyeTracker
from tobiiresearch.implementation.DisplayArea import DisplayArea
from tobii_research import EYETRACKER_GAZE_DATA

from eye_tracking.quadrant_calculator import QuadrantCalculator
from eye_tracking.local_storage import LocalStorage
from eye_tracking.gaze_data_callback import gaze_data_callback, get_gaze_data

class EyeTrackerController:
    def __init__(self, eye_tracker: EyeTracker):
        self.eye_tracker = eye_tracker

    def subscribe_with_callback(self) -> None:
        if self.eye_tracker is None:
            return
        self.eye_tracker.subscribe_to(EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

    def create_visualization(self, visualization_data):
        if self.eye_tracker is None:
            from simulated_data import simulated_data
            return simulated_data()
        else:
            print(get_gaze_data())
        print(visualization_data)

    def unsubscribe(self) -> None:
        if self.eye_tracker is None:
            return
        self.eye_tracker.unsubscribe_from(EYETRACKER_GAZE_DATA, gaze_data_callback)
