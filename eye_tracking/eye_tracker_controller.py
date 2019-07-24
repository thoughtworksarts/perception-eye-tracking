from tobiiresearch.implementation.EyeTracker import EyeTracker
from tobiiresearch.implementation.DisplayArea import DisplayArea
from tobii_research import EYETRACKER_GAZE_DATA

from eye_tracking.quadrant_calculator import QuadrantCalculator
from eye_tracking.local_storage import LocalStorage


class EyeTrackerController:
    def __init__(self, eye_tracker: EyeTracker, display_area: DisplayArea,
                 local_storage: LocalStorage, quadrant_calculator: QuadrantCalculator):
        self.eye_tracker = eye_tracker
        self.eye_tracker.set_display_area(display_area)
        self.local_storage = local_storage
        self.quadrant_calculator = quadrant_calculator

    def subscribe_with_callback(self, gaze_data_callback) -> None:
        self.eye_tracker.subscribe_to(EYETRACKER_GAZE_DATA, gaze_data_callback)

    def get_quadrant(self):
        eye_data = self.local_storage.get()
        self.quadrant_calculator.calculate_quadrant(eye_data)

    def unsubscribe(self) -> None:
        self.eye_tracker.unsubscribe_from(EYETRACKER_GAZE_DATA)
