import json

from flask import Flask, Response

from eye_tracking.eye_tracker_controller_factory import EyeTrackerControllerFactory

app = Flask(__name__)


@app.route('/start_eye_tracking')
def start_eye_tracking(level_id):
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='a+')
    eye_tracking_controller.subscribe_with_callback(level_id)
    return Response(status=200, response='Success')


@app.route('/stop_eye_tracking')
def stop_eye_tracking(level_id):
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='r')
    eye_tracking_controller.unsubscribe()
    return Response(status=200, response='Success')

@app.route('/create_eye_tracking_visualization')
def create_eye_tracking_visualization(levels):
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='r')
    return eye_tracking_controller.create_eye_tracking_visualization(levels)


if __name__ == '__main__':
    app.run(debug=True)
