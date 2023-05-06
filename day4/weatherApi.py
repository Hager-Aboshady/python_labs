import requests
class WeatherAPIClient:
        
    base_url = "https://api.weatherapi.com/v1/"
    api_key = "93b3e649ae85471587b121510230205"
    city = "Cairo"



    def get_current_temperature(self, city):
        url = f"{self.base_url}current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data["current"]["temp_c"]
            return temperature
        else:
            print(f"Error: Failed to get current temperature for {city}.")
            return None

    def get_temperature_after(self, city, days, hour=None):
        url = f"{self.base_url}forecast.json?key={self.api_key}&q={city}&days={days}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            forecast_days = data["forecast"]["forecastday"]
            temperatures = []
            for forecast_day in forecast_days:
                forecast_hour = forecast_day["hour"]
                for hourly_forecast in forecast_hour:
                    if hour is None or hourly_forecast["time"][-5:-3] == hour:
                        temperatures.append(hourly_forecast["temp_c"])
            return temperatures
        else:
            print(f"Error: Failed to get temperature forecast for {city}.")
            return None

    def get_lat_and_long(self, city):
        url = f"{self.base_url}forecast.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            lat = data["location"]["lat"]
            long = data["location"]["lon"]
            return (lat, long)
        else:
            print(f"Error: Failed to get latitude and longitude for {city}.")
            return None