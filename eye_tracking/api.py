import json

from flask import Flask, Response, request

from eye_tracking.eye_tracker_controller_factory import EyeTrackerControllerFactory

app = Flask(__name__)


@app.route('/eye-tracking/start', methods=['POST']) # levelId, startTime, stopTime
def start_eye_tracking():
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='a+')
    eye_tracking_controller.subscribe_with_callback(request.form['levelId'])
    return Response(status=200, response='Success')


@app.route('/eye-tracking/stop', methods=['POST']) # levelId
def stop_eye_tracking():
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='r')
    eye_tracking_controller.unsubscribe()
    return Response(status=200, response='Success')

@app.route('/eye-tracking/visualization', methods=['POST'])
def create_eye_tracking_visualization():
    eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='r')
    return eye_tracking_controller.create_eye_tracking_visualization(request.args['levels'])

if __name__ == '__main__':
    app.run(debug=True)
