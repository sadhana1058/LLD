from abc import ABC, abstractmethod
class WeatherProvider(ABC):
    @abstractmethod
    def fetch_weather(city):
        pass
class OpenWeatherMapProvider(WeatherProvider):
    def fetch_weather(self, city: str) -> str:
        print(f"Calling OpenWeatherMap API for: {city}")
        return "Sunny, 25C"

class WeatherStackProvider(WeatherProvider):
    def fetch_weather(self, city: str) -> str:
        print(f"Calling Weatherstack API for: {city}")
        return "Cloudy, 18C"

class WeatherApp:
    def __init__(self,api:WeatherProvider):
        self.api = api

    def display_weather(self, city: str) -> None:
        weather = self.api.fetch_weather(city)
        print(f"Weather in {city}: {weather}")

if __name__ == "__main__":
    wp = OpenWeatherMapProvider()
    app = WeatherApp(wp)
    print('--- OpenWeatherMap ---')
    app.display_weather("London")

    print()
    print('--- WeatherStack ---')
    ws = WeatherStackProvider()
    app2 = WeatherApp(ws)
    app2.display_weather("London")

# TODO: Create a WeatherProvider ABC with a get_weather(city) method.
# TODO: Refactor WeatherApp to accept a WeatherProvider via its constructor.