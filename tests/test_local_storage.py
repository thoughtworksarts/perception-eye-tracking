import os

from eye_tracking.local_storage import LocalStorage


class TestLocalStorage:

    def test_store_stores_data_correctly(self):
        test_data_file_path = 'tests/fixtures/test_stored_quadrant_data.txt'
        local_storage = LocalStorage(file_name=test_data_file_path, mode='a+')

        local_storage.store((0.1, 0.2), (0.3, 0.4))
        local_storage.close()

        with open(test_data_file_path, 'r') as file:
            data_line = file.readline()

            assert data_line == '0.1,0.2,0.3,0.4\n'

        os.remove(test_data_file_path)

    def test_get_returns_data_correctly(self):
        expected_result = [
            [(0.4145927429199219, 0.12054994702339172), (0.36220523715019226, 0.06620213389396667)],
            [(0.3883161246776581, 0.11936303973197937), (0.3348102569580078, 0.0703316181898117)],
            [(None, None), (None, None)],
            [(0.4441967308521271, -0.17462286353111267), (None, None)]
        ]

        local_storage = LocalStorage(file_name='tests/fixtures/test_quadrant_data.txt', mode='r')

        quadrant_data = local_storage.get()

        assert quadrant_data == expected_result
