class LocalStorage:

    def __init__(self, file_name, mode):
        self.eye_tracking_data_file = open(file_name, mode)

    def store(self, left_eye_coordinates, right_eye_coordinates):
        print(left_eye_coordinates, right_eye_coordinates)
        self.eye_tracking_data_file.writelines('{}, {}, {}, {}\n'.format(
            left_eye_coordinates[0], left_eye_coordinates[1],
            right_eye_coordinates[0], right_eye_coordinates[1])
        )

    def close(self):
        self.eye_tracking_data_file.close()

    def get(self):
        data = self.eye_tracking_data_file.readlines()
        result = []
        data = [line.strip() for line in data]

        for data_line in data:

            data_strings = data_line.split(',')
            data = [float(d) for d in data_strings]
            result.append([(data[0], data[1]), (data[2], data[3])])

        return result
