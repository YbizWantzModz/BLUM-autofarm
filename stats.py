class FarmStats:
    def __init__(self):
        self.clicks = 0

    def increment_clicks(self):
        self.clicks += 1

    def get_clicks(self):
        return self.clicks
