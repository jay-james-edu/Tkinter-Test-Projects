class TemperatureModel:

    def __init__(self):
        self._celsius = 0.0

    def set_celsius(self, celsius_str: str) -> bool:

        try:
            self._celsius = float(celsius_str)
            return True
        except ValueError:
            return False

    def get_celsius(self) -> float:
        return self._celsius

    def celsius_to_fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32
