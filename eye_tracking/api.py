import json

from flask import Flask, Response
from tobii_research import find_all_eyetrackers
from tobiiresearch.implementation.DisplayArea import DisplayArea

from eye_tracking.eye_tracker_controller import EyeTrackerController
from eye_tracking.gaze_data_callback import gaze_data_callback
from eye_tracking.config import DISPLAY_AREA_CONFIG
from eye_tracking.local_storage import LocalStorage
from eye_tracking.config import EYE_TRACKING_DATA_FILENAME
from eye_tracking.quadrant_calculator import QuadrantCalculator

app = Flask(__name__)

eye_trackers = find_all_eyetrackers()
eye_tracker = eye_trackers[0]

display_area = DisplayArea(DISPLAY_AREA_CONFIG)

eye_tracker.set_display_area(display_area)
eye_tracking_controller = EyeTrackerController(eye_tracker=eye_tracker, display_area=display_area)


@app.route('/start_eye_tracking')
def start_eye_tracking():
    # TODO: maybe add try/catch around this line
    eye_tracking_controller.subscribe_with_callback(gaze_data_callback)
    return Response(status=200, response='Success')


@app.route('/stop_eye_tracking')
def stop_eye_tracking():
    local_storage = LocalStorage(file_name=EYE_TRACKING_DATA_FILENAME)
    quadrant_calculator = QuadrantCalculator(local_storage)
    quadrant = quadrant_calculator.calculate_quadrant()
    eye_tracking_controller.unsubscribe()
    return Response(status=200, response=json.dumps({'quadrant': quadrant}),)


if __name__ == '__main__':
    app.run(debug=True)
