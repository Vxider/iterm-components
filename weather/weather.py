from subprocess import STDOUT, check_output
import asyncio
import iterm2
import json
import re
import urllib.request

def get_weather_icon(weather):
    if re.match(r'clear*', weather):
        return '☀️'
    elif re.match(r'cloud*', weather):
        return '☁️'
    elif re.match(r'fog|haze*|mist*', weather):
        return '🌫'
    elif re.match(r'partly-cloudy*', weather):
        return '⛅️'
    elif re.match(r'rain', weather):
        return '🌧️'
    elif re.match(r'sleet|snow', weather):
        return '🌨'
    elif re.match(r'thunderstorm', weather):
        return '⛈'
    elif re.match(r'tornado', weather):
        return '🌪️'
    elif re.match(r'wind', weather):
        return '🌬'
    else:
        return '?'

def get_temperature(temp):
    if re.match(r'fahrenheit|us', temp):
        return '°F'
    else:
        return '°C'

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Weather',
        detailed_description='Display weather by using darksky-weather',
        exemplar='🌧️8°C',
        update_cadence=900,
        identifier='vxider.iterm-components.weather',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def weather_coroutine(knobs):
        try:
            output = check_output(["/usr/local/bin/weather", "-json"], stderr=STDOUT, timeout=10)
            data = json.loads(output.decode().strip())
            weather=data['currently']['temperature']
            icon_text=data['currently']['icon']
            unit=data['flags']['units']
            return f'{get_weather_icon(icon_text)}{int(weather)}{get_temperature(unit)}'
        except Exception as e:
            print(e)
            return '☁️ N/A'

    await component.async_register(connection, weather_coroutine, timeout=15)

iterm2.run_forever(main)
