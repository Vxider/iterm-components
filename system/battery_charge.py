import asyncio
import iterm2
import re

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Battery Charge',
        detailed_description='This plugin displays the current battery charge.(requires iStats ruby gem)',
        exemplar='\uF581 90%',
        update_cadence=5,
        identifier='vxider.iterm-components.battery_charge',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def battery_charge_coroutine(knobs):
        proc = await asyncio.create_subprocess_shell(
            "/usr/bin/pmset -g batt",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        status = stdout.decode().strip();
        icon = None
        estimate = None
        percentage = None
        if ("charged" in status):
            icon='\uf578'
            return f'{icon}' if not stderr else '\uF582 N/A'
        else:
            percentage = re.search('[0-9]*%', status).group(0)[:-1]
            if ("no estimate" in status):
                estimate = 'no estimate'
            else:
                estimate = re.search('[0-9]+:[0-9]+', status).group(0)

            charge_icons=None
            if ("discharging" in status):
                charge_icons="\uF586 \uf579 \uf57a \uf57b \uf57c \uf57d \uf57e \uf57f \uf580 \uf581 \uf578 "
            else:
                charge_icons="\uF585 \uf585 \uf585 \uf586 \uf587 \uf587 \uf588 \uf588 \uf589 \uf58a \uf584 "
            if percentage == "100":
                icon = "\uf578"
            else:
                icon=charge_icons.split()[ord(percentage[0]) - 48]
            return f'{icon} {percentage}% {estimate}' if not stderr else '\uF582 N/A'

    await component.async_register(connection, battery_charge_coroutine)

iterm2.run_forever(main)
