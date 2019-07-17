from tobiiresearch.implementation.EyeTracker import EyeTracker
from tobiiresearch.implementation.DisplayArea import DisplayArea


class EyeTrackerController:
    def __init__(self, eye_tracker: EyeTracker, display_area: DisplayArea):
        self.eye_tracker = eye_tracker
        self.eye_tracker.set_display_area(display_area)

    def subscribe_with_callback(self, gaze_data_callback):
        self.eye_tracker.subscribe_to(self.eye_tracker.EYE_TRACKER_GAZEDATA, gaze_data_callback)




