

def execute(eyetracker):
    if eyetracker is None:
        return
    filename = "saved_calibration.bin"

    with open(filename, "wb") as f:
        calibration_data = eyetracker.retrieve_calibration_data()

        if calibration_data is not None:
            print("Saving calibration to file for eye tracker with serial number {0}.".format(eyetracker.serial_number))
            f.write(eyetracker.retrieve_calibration_data())
        else:
            print("No calibration available for eye tracker with serial number {0}.".format(eyetracker.serial_number))

    with open(filename, "rb") as f:
        calibration_data = f.read()

        if len(calibration_data) > 0:
            print("Applying calibration on eye tracker with serial number {0}.".format(eyetracker.serial_number))
            eyetracker.apply_calibration_data(calibration_data)

        import os

        try:
            os.remove(filename)
        except OSError:
            pass

# execute(find_all_eyetrackers()[0])