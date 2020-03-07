import asyncio
import iterm2
import json
import urllib.request

TOKEN="XXXXXXXXXXXXXXXXXXXXXXX"
CITY="Beijing"

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='AQI',
        detailed_description='Air Quality Index',
        exemplar='😷80',
        update_cadence=900,
        identifier='vxider.iterm-components.aqi',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def aqi_coroutine(knobs):
        url = "http://api.waqi.info/feed/" + CITY + "/?token=" + TOKEN
        try:
            request = urllib.request.Request( url, {})
            aqi = json.loads(
                urllib.request.urlopen(request).read().decode()
            )['data']['aqi']
            return f'😷{aqi}'
        except:
            raise
        else:
            return f'😷N/A'

    await component.async_register(connection, aqi_coroutine)

iterm2.run_forever(main)
