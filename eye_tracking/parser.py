from typing import Tuple

from tobiiresearch.implementation.GazeData import EyeData


class Parser:
    def parse(self, eye_data: EyeData) -> Tuple:
        return eye_data.gaze_point.position_on_display_area
