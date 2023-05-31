import requests
import numpy as np
import matplotlib.pylab as plt


def open_meteo(latitude, longitude):
    """Create the meteo API request and return it if we have successful status code"""
    try:
        # useless variables but we need to check if we can convert the values to float
        lat = float(latitude)
        lon = float(longitude)
    except ValueError as err:
        print(
            f"Please provide float inputs for latitude and longitude. (inputs: {latitude} | {longitude})")

        return None

    meteo_url = f"https://api.open-meteo.com/v1/forecast?latitude={str(latitude)}&longitude={str(longitude)}&hourly=temperature_2m"
    response = requests.get(meteo_url)

    if response.status_code == 200:
        print("Successful connection to meteo API.")
        print('-------------------------------')
        data = response.json()

        return data
    else:
        print("Unable to create the API request!")

        return None


def plot_data(data):
    """Plot the data we received from the meteo API request"""
    # time = data.get('hourly', {}).get('time')
    temperature = data.get('hourly', {}).get('temperature_2m')

    # x=time[:24] not needed actually
    y = temperature[:24]

    x = list(range(0, 24))

    plt.plot(x, y)

    plt.xlabel("Hour")
    plt.ylabel("Temperature")

    plt.xticks(x)
    plt.yticks(np.arange(int(min(y)), int(max(y)) + 1, 1.0))

    plt.show()


if __name__ == "__main__":
    # get input data
    lat = input("Enter latitude")
    lon = input("Enter longitude")

    # create the meteo request with the input data
    meteo_data = open_meteo(latitude=lat, longitude=lon)

    plot_data(meteo_data)
