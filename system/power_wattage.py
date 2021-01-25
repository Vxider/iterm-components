import asyncio
import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='power_wattage',
        detailed_description='The power dapter wattage currently connected',
        exemplar='\uFBA3 100W',
        update_cadence=5,
        identifier='vxider.iterm-components.power_wattage',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def power_wattage_coroutine(knobs):
        proc = await asyncio.create_subprocess_shell(
            '/usr/sbin/system_profiler SPPowerDataType | grep "Wattage" | awk "{print \$3}"',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if not stdout or stderr:
            return '\uFBA4'
        return f'\uFBA3 {stdout.decode().strip()}W'

    await component.async_register(connection, power_wattage_coroutine)

iterm2.run_forever(main)
