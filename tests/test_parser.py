from unittest.mock import MagicMock

import pytest
from tobiiresearch.implementation.GazeData import EyeData, GazePoint

from eye_tracking.parser import Parser


class TestParser:
    @pytest.mark.parametrize('coordinates', [(0, 0), (10, 20), (-30, 50), (-30, -20), (None, 3)])
    def test_parse_successfully_returns_coordinates(self, coordinates):
        gaze_point_mock = MagicMock(spec=GazePoint)
        gaze_point_mock.position_on_display_area = coordinates

        eye_data_mock = MagicMock(spec=EyeData)
        eye_data_mock.gaze_point = gaze_point_mock

        parser = Parser()

        parsed_coordinates = parser.parse(eye_data_mock)

        assert parsed_coordinates == coordinates

