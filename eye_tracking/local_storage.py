from eye_tracking.parser import Parser


class LocalStorage:

    def __init__(self, file_name: str, mode: str):
        self.eye_tracking_data_file = open(file_name, mode)

    def store(self, left_eye_coordinates: tuple, right_eye_coordinates: tuple) -> None:
        #print(left_eye_coordinates, right_eye_coordinates)
        self.eye_tracking_data_file.writelines('{},{},{},{}\n'.format(
            left_eye_coordinates[0], left_eye_coordinates[1],
            right_eye_coordinates[0], right_eye_coordinates[1])
        )

    def close(self) -> None:
        self.eye_tracking_data_file.close()

    def get(self) -> list:
        data = self.eye_tracking_data_file.readlines()
        result = []
        data = [line.strip() for line in data]

        for stored_data_row in data:
            parser = Parser(stored_data_row.split(','))
            eye_data_tuples = parser.get_coordinates_from_stored_data()
            result.append(eye_data_tuples)

        return result
