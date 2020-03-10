import asyncio
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Fan Speed',
        detailed_description='This plugin displays the current Fan speed.(requires iStats ruby gem)',
        exemplar='\uf70f 2000/2000RPM',
        update_cadence=5,
        identifier='vxider.iterm-components.fan_speed',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def fan_speed_coroutine(knobs):
        proc = await asyncio.create_subprocess_shell(
            "/Users/vxider/.rbenv/shims/istats fan speed --value-only | tr '\n' '/' | sed 's/.$//;s/ //g'",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        return f'\uf70f {stdout.decode().strip()}RPM' if not stderr else '\uf70f N/A'

    await component.async_register(connection, fan_speed_coroutine)

iterm2.run_forever(main)
