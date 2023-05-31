import requests
import numpy as np
import matplotlib.pylab as plt
import unittest

def open_meteo(latitude, longitude):
    """Create the meteo API request and return it if we have successful status code"""
    try:
        # useless variables but we need to check if we can convert the values to float
        lat = float(latitude)
        lon = float(longitude)
    except ValueError as e:
        print(f"Please provide float inputs for latitude and longitude. (inputs: {latitude} | {longitude})")

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
    
class TestMeteoAPI(unittest.TestCase):
    def test_open_meteo(self):
        # Test with valid inputs
        data = open_meteo(51.52, 5.48)
        self.assertIsNotNone(data)
        #self.assertTrue(isinstance(data, dict))

         # Test with invalid inputs
        data = open_meteo('51.5072', '-0.1276')  # string instead of float
        self.assertIsNone(data)
    def test_plot_data(self):
        # Test with valid data
        data = {'hourly': {'temperature_2m': [10, 12, 15, 16, 18, 21, 22, 20, 18, 16, 14, 12, 10, 10, 8, 7, 6, 6, 5, 4, 3, 3, 2, 2]}}
        plot_data(data)
        self.assertTrue(True) # We can't actually test if the plot is correct, so just make sure the function doesn't throw an error

        # Test with missing data
        data = {'wrong': 'data'}
        with self.assertRaises(AttributeError):
            plot_data(data)

if __name__ == "__main__":
    unittest.main()
