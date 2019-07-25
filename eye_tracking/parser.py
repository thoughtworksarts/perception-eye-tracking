from typing import Tuple

from tobiiresearch.implementation.GazeData import EyeData


class Parser:

    def __init__(self, stored_data_row: list):
        self.left_eye_x_coordinate = float(stored_data_row[0]) if stored_data_row[0] != 'nan' else None
        self.left_eye_y_coordinate = float(stored_data_row[1]) if stored_data_row[1] != 'nan' else None
        self.right_eye_x_coordinate = float(stored_data_row[2]) if stored_data_row[2] != 'nan' else None
        self.right_eye_y_coordinate = float(stored_data_row[3]) if stored_data_row[3] != 'nan' else None

    @staticmethod
    def get_coordinates_from_eye_data(eye_data: EyeData) -> Tuple:
        return eye_data.gaze_point.position_on_display_area

    def get_coordinates_from_stored_data(self) -> list:
        return [
            (self.left_eye_x_coordinate, self.left_eye_y_coordinate),
            (self.right_eye_x_coordinate, self.right_eye_y_coordinate)
        ]
