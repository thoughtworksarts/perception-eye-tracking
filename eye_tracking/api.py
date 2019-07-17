from flask import Flask, Response
import tobii_research
from tobiiresearch.implementation.DisplayArea import DisplayArea

from eye_tracking.eye_tracker_controller import EyeTrackerController
from eye_tracking.gaze_data_callback import gaze_data_callback
from eye_tracking.config import DISPLAY_AREA_CONFIG

app = Flask(__name__)

eye_tracker = tobii_research.find_all_eyetrackers()[0]

display_area = DisplayArea(DISPLAY_AREA_CONFIG)

eye_tracker_controller = EyeTrackerController(eye_tracker=eye_tracker, display_area=display_area)


@app.route('/start_eye_tracking')
def start_eye_tracking():
    # TODO: maybe add try/catch around this line
    eye_tracker_controller.subscribe_with_callback(gaze_data_callback)
    return Response(status=200, response='Success')


@app.route('/stop_eye_tracking')
def stop_eye_tracking():
    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run(debug=True)
