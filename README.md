# WiFi-connected Dolar to Turkish Lira to the LCD Screen

This project utilizes a microcontroller to display exchange rates of major currencies.

## Requirements

To run this project, you will need the following components:

- Microcontroller compatible with MicroPython (e.g., ESP8266, ESP32, Raspberry Pi Pico W)
- LCD display
- LCD adapter with I2C interface
- Wi-Fi connection

## Installation

1. Download or clone the project files into a folder.
2. Flash the MicroPython firmware onto the microcontroller(In this project, Raspberry Pi Pico-W).
3. Download and install the required libraries onto the microcontroller.
4. Make the necessary connections: Connect the LCD display and I2C adapter to the microcontroller.
5. Enter your Wi-Fi network's SSID and password into the appropriate variables.

## API

This project utilizes the Genel Para API to retrieve exchange rates. The API used in this project is provided by Genel Para and can be accessed at the following endpoint:

- API URL: `https://api.genelpara.com/embed/doviz.json`

The API provides exchange rate data for various currencies, including USD, EUR, GBP, etc.

Please note that you may need to sign up or obtain an API key from Genel Para to use their API effectively. Refer to the Genel Para API documentation for more details on accessing and using the API.

## Usage

1. Power up the microcontroller.
2. The current exchange rate for USD will be displayed on the LCD screen.
3. The value will be updated every 60 seconds.

## Contributing

1. Fork this project.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and save: `git commit -am 'Description of your changes'`
4. Push to your branch: `git push origin my-feature-branch`
5. Open a new Pull Request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
