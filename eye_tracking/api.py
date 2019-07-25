import json

from flask import Flask, Response

from eye_tracking.gaze_data_callback import gaze_data_callback
from eye_tracking.eye_tracker_controller_factory import EyeTrackerControllerFactory

app = Flask(__name__)


@app.route('/start_eye_tracking')
def start_eye_tracking():
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='a+')
    eye_tracking_controller.subscribe_with_callback(gaze_data_callback)
    return Response(status=200, response='Success')


@app.route('/stop_eye_tracking')
def stop_eye_tracking():
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='r')

    quadrant = eye_tracking_controller.get_quadrant()
    eye_tracking_controller.unsubscribe()
    return Response(status=200, response=json.dumps({'quadrant': quadrant}))


if __name__ == '__main__':
    app.run(debug=True)
