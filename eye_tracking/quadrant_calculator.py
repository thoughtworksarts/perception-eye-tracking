from eye_tracking.local_storage import LocalStorage


class QuadrantCalculator:

    def __init__(self, local_storage: LocalStorage):
        self.local_storage = local_storage

    def calculate_quadrant(self):
        quadrant_data = self.local_storage.get()
        return quadrant_data
