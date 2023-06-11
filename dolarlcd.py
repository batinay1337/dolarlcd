import urequests as requests
import time
import network
import socket
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

lcd = I2cLcd(i2c, 0x27, 2, 16)

# Wi-Fi connect
ssid = 'WiFiName'
password = 'password'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )


# API URL
api_url = 'https://api.genelpara.com/embed/doviz.json'

def get_dolar_value():
    try:
        response = requests.get(api_url)
        data = response.json()
        #return float(data[0]['data']['value'])
        #current_USD_value = (data[0]['data']['value'])
        current_USD_value = (data["USD"]["satis"])
        
        return current_USD_value
        
    except KeyError:
        print('There is illegal data in your API response.')
        return None

def display_dolar_value():
    dolar_value = get_dolar_value()
    if dolar_value is not None:
        lcd.clear()
        lcd.putstr('Dolar: ' + str(dolar_value))

try:
    while True:
        display_dolar_value()
        time.sleep(60)  # updating every 60 seconds

except KeyboardInterrupt:
    pass
