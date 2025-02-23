import requests


API_KEY = "61877257d391c8bafff6fa01b3a7b170"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    n_values = 8 * forecast_days
    filtered_data = filtered_data[:n_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place="Tokyo", forecast_days=3))