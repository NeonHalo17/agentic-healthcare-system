class Metrics:

    def __init__(self):
        self.total_cases = 0
        self.correct_answers = 0
        self.booking_attempts = 0
        self.booking_successes = 0
        self.total_latency = 0.0

    def add_case(self, passed: bool, latency: float):
        self.total_cases += 1

        if passed:
            self.correct_answers += 1
        self.total_latency += latency

    def add_booking(self, success: bool):
        self.booking_attempts += 1
        if success:
            self.booking_successes += 1

    def summary(self):
        return {
            "total_cases": self.total_cases,
            "accuracy":
                self.correct_answers / self.total_cases
                if self.total_cases else 0,
            "average_latency":
                self.total_latency / self.total_cases
                if self.total_cases else 0,
            "booking_success_rate":
                self.booking_successes /
                self.booking_attempts
                if self.booking_attempts else 0
        }
