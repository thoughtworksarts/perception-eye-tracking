from typing import Tuple

from tobiiresearch.implementation.GazeData import EyeData


class Parser:

    def __init__(self, data_line_string: list):
        self.left_eye_x_coordinate = float(data_line_string[0]) if data_line_string[0] != 'nan' else None
        self.left_eye_y_coordinate = float(data_line_string[1]) if data_line_string[1] != 'nan' else None
        self.right_eye_x_coordinate = float(data_line_string[2]) if data_line_string[2] != 'nan' else None
        self.right_eye_y_coordinate = float(data_line_string[3]) if data_line_string[3] != 'nan' else None

    @staticmethod
    def get_coordinates_from_eye_data(eye_data: EyeData) -> Tuple:
        return eye_data.gaze_point.position_on_display_area

    def get_coordinates_from_stored_data(self):
        return [
            (self.left_eye_x_coordinate, self.left_eye_y_coordinate),
            (self.right_eye_x_coordinate, self.right_eye_y_coordinate)
        ]
