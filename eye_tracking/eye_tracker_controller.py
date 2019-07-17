class EyeTrackerController:
    def __init__(self, display_area, eye_tracker):
        self.display_area = display_area
        self.eye_tracker = eye_tracker

    def set_display_area(self, display_area):
        self.display_area = display_area

    def get_eye_tracker(self):
        return self.eye_tracker

    def subscribe_with_callback(self, gaze_data_callback):
        self.eye_tracker.subscribe_to(self.eye_tracker.EYE_TRACKER_GAZEDATA, gaze_data_callback, as_dictionary=True)




