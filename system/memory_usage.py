import asyncio
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Memory Usage',
        detailed_description='This plugin displays the current memory usage.',
        exemplar='\uf85a 88%',
        update_cadence=5,
        identifier='vxider.iterm-components.mem_usage',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def mem_usage_coroutine(knobs):
        proc = await asyncio.create_subprocess_shell(
            "ps -A -o %mem | awk '{ mem += $1} END {print mem}'",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        percentage = stdout.decode().strip().split('.')[0];
        return f'\uf85a {percentage}%' if not stderr else '\uf85a N/A'

    await component.async_register(connection, mem_usage_coroutine)

iterm2.run_forever(main)
