import json

from flask import Flask, Response, request

from eye_tracking.eye_tracker_controller_factory import EyeTrackerControllerFactory

app = Flask(__name__)
eye_tracking_controller = EyeTrackerControllerFactory.get_eye_tracker_controller(mode='a+')

@app.route('/eye-tracking/start', methods=['POST'])
def start_eye_tracking():
    eye_tracking_controller.subscribe_with_callback()
    return Response(status=200, response='Success')

@app.route('/eye-tracking/stop', methods=['POST'])
def stop_eye_tracking():
    eye_tracking_controller.unsubscribe()
    return Response(status=200, response='Success')

@app.route('/visualization', methods=['POST'])
def create_eye_tracking_visualization():
    return eye_tracking_controller.create_eye_tracking_visualization(json.loads(request.data))

if __name__ == '__main__':
    app.run(debug=True)
