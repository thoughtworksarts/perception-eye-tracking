from tobiiresearch.implementation.EyeTracker import EyeTracker
from tobiiresearch.implementation.DisplayArea import DisplayArea
from tobii_research import EYETRACKER_GAZE_DATA

from eye_tracking.quadrant_calculator import QuadrantCalculator
from eye_tracking.local_storage import LocalStorage
from eye_tracking.gaze_data_callback import gaze_data_callback
from eye_tracking.get_gaze_data_by_level_id import get_gaze_data

class EyeTrackerController:
    def __init__(self, eye_tracker: EyeTracker, display_area: DisplayArea,
                 local_storage: LocalStorage, quadrant_calculator: QuadrantCalculator):
        self.eye_tracker = eye_tracker
        self.eye_tracker.set_display_area(display_area)
        self.local_storage = local_storage
        self.quadrant_calculator = quadrant_calculator

    def subscribe_with_callback(self, level_id) -> None:
        self.eye_tracker.subscribe_to(EYETRACKER_GAZE_DATA, gaze_data_callback)

    def create_eye_tracking_visualization(self, levels):
        file_name = generate_filename()
        create_data_visualization(file_name, get_levels_with_gaze_data(levels, get_gaze_data_by_level_id(get_level_ids(levels))))
        return file_name

    def get_level_ids(levels):
        return [level.id for level in levels]
    
    def get_levels_with_gaze_data(levels, gaze_data_by_level_id):
        for level in levels:
            level.gaze_data = gaze_data_by_level_id[level.id]
        return levels

    def get_gaze_data_by_level_id(level_ids):
        gaze_data_by_level_id = {}
        for level_id in level_ids:
            gaze_data_by_level_id[level_id] = get_gaze_data(level_id)
        return gaze_data_by_level_id
    
    def generate_filename():
        return 'hue'
    
    def create_data_visualization(file_name, gaze_data_by_level_id):
        print(hue)

    def unsubscribe(self) -> None:
        self.eye_tracker.unsubscribe_from(EYETRACKER_GAZE_DATA)
