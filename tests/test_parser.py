from unittest.mock import MagicMock

import pytest
from tobiiresearch.implementation.GazeData import EyeData, GazePoint

from eye_tracking.parser import Parser


class TestParser:
    @pytest.mark.parametrize('coordinates', [(0, 0), (10, 20), (-30, 50), (-30, -20), (None, 3)])
    def test_get_coordinates_from_eye_data_is_successful(self, coordinates):
        gaze_point_mock = MagicMock(spec=GazePoint)
        gaze_point_mock.position_on_display_area = coordinates

        eye_data_mock = MagicMock(spec=EyeData)
        eye_data_mock.gaze_point = gaze_point_mock

        parsed_coordinates = Parser.get_coordinates_from_eye_data(eye_data_mock)

        assert parsed_coordinates == coordinates

    @pytest.mark.parametrize('eye_data_strings,expected_coordinates', [
        (['0.23', '0.24', '0.94', '0.21'], [(0.23, 0.24), (0.94, 0.21)]),
        (['0.23', 'nan', '0.94', 'nan'], [(0.23, None), (0.94, None)]),
        (['0.123456', '0.2468', '0.9876', 'nan'], [(0.123456, 0.2468), (0.9876, None)]),
    ])
    def test_get_coordinates_from_stored_data_is_successful(self, eye_data_strings, expected_coordinates):

        expected_coordinates = expected_coordinates

        parser = Parser(eye_data_strings)
        coordinates = parser.get_coordinates_from_stored_data()

        assert coordinates == expected_coordinates
