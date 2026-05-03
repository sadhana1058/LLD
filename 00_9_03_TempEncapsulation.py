class TemperatureSensor:
    def __init__(self):
        self._readings: list[float] = []

    def add_reading(self, value: float) -> None:
        # Only add if value is between -50 and 150 (inclusive)
        if value>= -50 and value<=150:
            self._readings.append(value)

        

    def get_average(self) -> float:
        # Return the average of all readings, or 0.0 if no readings 
        if self._readings:
            return sum(self._readings)/len(self._readings)
        return 0.0

    def get_reading_count(self) -> int:
        # Return how many readings have been recorded
        return len(self._readings)

    def get_readings(self) -> list[float]:
        # Return a copy of the readings list (not the original)
        c = self._readings.copy()
        return c


if __name__ == "__main__":
    sensor = TemperatureSensor()
    sensor.add_reading(22.5)
    sensor.add_reading(23.1)
    sensor.add_reading(200.0)  # Should be rejected
    sensor.add_reading(-10.0)

    print(f"Count: {sensor.get_reading_count()}")  # 3
    print(f"Average: {sensor.get_average()}")       # 11.87