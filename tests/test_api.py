from unittest.mock import patch, MagicMock

from eye_tracking.api import app
from eye_tracking.eye_tracker_controller import EyeTrackerController
from eye_tracking.gaze_data_callback import gaze_data_callback


class TestApi:

    @patch('eye_tracking.api.EyeTrackerControllerFactory')
    def test_start_eye_tracking(self, eye_tracker_controller_factory_mock):
        eye_tracker_controller_mock = MagicMock(spec=EyeTrackerController)
        eye_tracker_controller_factory_mock.get_eye_tracker_controller.return_value = eye_tracker_controller_mock
        test_client = app.test_client()

        response = test_client.get('/start_eye_tracking')

        eye_tracker_controller_mock.subscribe_with_callback.called_once_with(gaze_data_callback)
        assert response.status_code == 200
        assert response.data == b'Success'

    @patch('eye_tracking.api.EyeTrackerControllerFactory')
    def test_stop_eye_tracking(self, eye_tracker_controller_factory_mock):

        eye_tracker_controller_mock = MagicMock(spec=EyeTrackerController)
        eye_tracker_controller_factory_mock.get_eye_tracker_controller.return_value = eye_tracker_controller_mock
        eye_tracker_controller_mock.get_quadrant.return_value = 1

        test_client = app.test_client()
        response = test_client.get('/stop_eye_tracking')

        eye_tracker_controller_mock.unsubscribe.called_once()
        eye_tracker_controller_mock.get_quadrant.called_once()

        assert response.status_code == 200
        assert response.data == b'{"quadrant": 1}'
