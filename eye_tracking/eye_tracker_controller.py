from tobiiresearch.implementation.EyeTracker import EyeTracker
from tobiiresearch.implementation.DisplayArea import DisplayArea
from tobii_research import EYETRACKER_GAZE_DATA


class EyeTrackerController:
    def __init__(self, eye_tracker: EyeTracker, display_area: DisplayArea):
        self.eye_tracker = eye_tracker
        self.eye_tracker.set_display_area(display_area)

    def subscribe_with_callback(self, gaze_data_callback):
        self.eye_tracker.subscribe_to(EYETRACKER_GAZE_DATA, gaze_data_callback)

    def unsubscribe(self):
        self.eye_tracker.unsubscribe_from(EYETRACKER_GAZE_DATA)
