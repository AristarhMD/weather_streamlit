import requests

API_KEY = "ca0d6db8e6065410fc2acdb2659d8fb8"


def get_data(place, forecast_days, data_choice):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    if data_choice == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if data_choice == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Chisinau", forecast_days=2, data_choice="Sky"))