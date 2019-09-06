global_gaze_data = []

def gaze_data_callback(gaze_data) -> None:
    global global_gaze_data
    print(gaze_data)
    global_gaze_data.append({
        "timestamp":gaze_data['system_time_stamp'],
        "gaze_left_eye":gaze_data['left_gaze_point_on_display_area'],
        "gaze_right_eye":gaze_data['right_gaze_point_on_display_area'],

    })

def get_gaze_data():
    global global_gaze_data
    return global_gaze_data


