from tobiiresearch.implementation.EyeTracker import EyeTracker
from tobiiresearch.implementation.DisplayArea import DisplayArea
from tobii_research import EYETRACKER_GAZE_DATA

from eye_tracking.quadrant_calculator import QuadrantCalculator
from eye_tracking.local_storage import LocalStorage
from eye_tracking.gaze_data_callback import gaze_data_callback, get_gaze_data

class EyeTrackerController:
    def __init__(self, eye_tracker: EyeTracker, display_area: DisplayArea,
                 local_storage: LocalStorage, quadrant_calculator: QuadrantCalculator):
        self.eye_tracker = eye_tracker
        self.eye_tracker.set_display_area(display_area)
        self.local_storage = local_storage
        self.quadrant_calculator = quadrant_calculator

    def subscribe_with_callback(self) -> None:
        self.eye_tracker.subscribe_to(EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

    def generate_filename(self):
        return 'hue'

    def create_eye_tracking_visualization(self, visualization_data):
        file_name = self.generate_filename()
        self.create_data_visualization(visualization_data, get_gaze_data())
        return file_name

    
    def create_data_visualization(self, visualization_data, gaze_data):
        print(gaze_data)
        print(visualization_data)

    def unsubscribe(self) -> None:
        self.eye_tracker.unsubscribe_from(EYETRACKER_GAZE_DATA, gaze_data_callback)
