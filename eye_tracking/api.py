import json

from flask import Flask, Response

from eye_tracking.gaze_data_callback import gaze_data_callback
from eye_tracking.local_storage import LocalStorage
from eye_tracking.config import EYE_TRACKING_DATA_FILENAME
from eye_tracking.quadrant_calculator import QuadrantCalculator
from eye_tracking.eye_tracker_controller_factory import EyeTrackerControllerFactory

app = Flask(__name__)


@app.route('/start_eye_tracking')
def start_eye_tracking():
    # TODO: maybe add try/catch around this line
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller()
    eye_tracking_controller.subscribe_with_callback(gaze_data_callback)
    return Response(status=200, response='Success')


@app.route('/stop_eye_tracking')
def stop_eye_tracking():
    local_storage = LocalStorage(file_name=EYE_TRACKING_DATA_FILENAME, mode='r')
    quadrant_calculator = QuadrantCalculator()

    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(
        local_storage=local_storage, quadrant_calculator=quadrant_calculator
    )

    quadrant = quadrant_calculator.calculate_quadrant()
    eye_tracking_controller.unsubscribe()
    return Response(status=200, response=json.dumps({'quadrant': quadrant}))


if __name__ == '__main__':
    app.run(debug=True)
