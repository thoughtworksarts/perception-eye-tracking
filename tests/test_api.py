from unittest.mock import patch, MagicMock

from tobiiresearch.implementation.EyeTracker import EyeTracker
from tobiiresearch.implementation.DisplayArea import DisplayArea

from eye_tracking.eye_tracker_controller import EyeTrackerController
from eye_tracking.api import app


# class TestApi:
#     @patch('eye_tracking.api.EyeTrackerController')
#     @patch('eye_tracking.api.DisplayArea')
#     @patch('eye_tracking.api.find_all_eyetrackers')
#     def test_start_eye_tracking_returns_succesfully(self, find_all_eyetrackers, display_area_constructor_mock, eye_tracker_controller_constructor_mock):
#         find_all_eyetrackers.return_value = (MagicMock(spec=EyeTracker))
#         display_area_constructor_mock.return_value = MagicMock(spec=DisplayArea)
#
#         eye_tracker_controller_mock = MagicMock(spec=EyeTrackerController)
#         eye_tracker_controller_constructor_mock.return_value = eye_tracker_controller_mock
#
#         test_client = app.test_client()
#         response = test_client.get('/start_eye_tracking')
#
#         assert eye_tracker_controller_mock.subscribe_to.was_called_once()
#         assert response.status_code == 200
