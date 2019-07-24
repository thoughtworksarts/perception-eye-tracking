
from tobii_research import find_all_eyetrackers
from tobiiresearch.implementation.DisplayArea import DisplayArea

from eye_tracking.eye_tracker_controller import EyeTrackerController
from eye_tracking.config import DISPLAY_AREA_CONFIG
from eye_tracking.local_storage import LocalStorage
from eye_tracking.quadrant_calculator import QuadrantCalculator
from eye_tracking.config import EYE_TRACKING_DATA_FILENAME


class EyeTrackerControllerFactory:

    @staticmethod
    def get_eye_tracker_controller():
        eye_trackers = find_all_eyetrackers()
        eye_tracker = eye_trackers[0]

        display_area = DisplayArea(DISPLAY_AREA_CONFIG)
        eye_tracker.set_display_area(display_area)

        local_storage = LocalStorage(file_name=EYE_TRACKING_DATA_FILENAME, mode='r')
        quadrant_calculator = QuadrantCalculator()

        return EyeTrackerController(eye_tracker=eye_tracker, display_area=display_area,
                                    local_storage=local_storage, quadrant_calculator=quadrant_calculator)
