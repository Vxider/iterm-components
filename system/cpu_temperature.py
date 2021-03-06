import asyncio
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='CPU Temperature',
        detailed_description='This plugin displays the current cpu temperature.(requires iStats ruby gem)',
        exemplar='\uf8c7 61°C',
        update_cadence=5,
        identifier='vxider.iterm-components.cpu_temperature',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def cpu_temp_coroutine(knobs):
        proc = await asyncio.create_subprocess_shell(
            # '~/.rbenv/shims/istats scan "TCXC PECI CPU" --value-only | cut -d \'.\' -f1', #use this line if you want to get CPU PECI temperature (Same temperature as in Intel Power Gadget.)
            '~/.rbenv/shims/istats cpu temp --value-only | cut -d \'.\' -f1', # use CPU proximity temperature
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        return f'\uf8c7 {stdout.decode().strip()}°C' if not stderr else '\uf8c7 N/A'

    await component.async_register(connection, cpu_temp_coroutine)

iterm2.run_forever(main)
