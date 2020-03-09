# iterm-components

Custom status bar components for use with iTerm2

![](screenshots/example.png)


# Table of Contents
<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Installation](#installation)
- [Components](#components)
  - [System](#system)
    - [Power wattage](#power-wattage)
    - [CPU temperature](#cpu-temperature)
    - [Fan speed](#fan-speed)
    - [Battery charge](#battery-charge)
  - [Weather](#weather)
    - [AQI](#aqi)
    - [Local Weather](#local-weather)
- [Configuration](#configuration)

<!-- /code_chunk_output -->


## Installation

1. Install script to iTerm2 by using `./install.sh`. Or copy the scripts you want to `~/Library/Application Support/iTerm2/Scripts/AutoLaunch`
2. Install [Nerd Font](https://www.nerdfonts.com/)
3. Select **Scripts > system|weather** in the iTerm2 menu bar and select the components you want to be available.
4. Drag the components where you like.
![components](screenshots/components.png)

## Components

### System

#### Power wattage

Display the AC power adapter wattage currently connected.

![power usage](screenshots/power-wattage.png)

#### CPU temperature

Display the CPU temperature. (Requires iStats ruby gem)

![CPU temperature](screenshots/cpu-temperature.png)

Install [iStats](https://github.com/Chris911/iStats) by `gem install iStats`

#### Fan speed

Display the fan speed. (Requires iStats ruby gem)

![fan speed](screenshots/fan-speed.png)

#### Battery charge

Display battery charge status and the estimate remaining time.

Charging:

![battery charge](screenshots/battery-charge-no-estimate.png)

![battery charge](screenshots/battery-charge-charging.png)

Charged:

![battery charge](screenshots/battery-charge-charged.png)

### Weather

#### AQI

You need an [aqi api token](https://aqicn.org/api/) and modify the `TOKEN` and `CITY` fields in `weather/aqi.py`.

![aqi](screenshots/aqi.png)

#### Local Weather

Display local weather by [darksky-weather](https://github.com/genuinetools/weather).

Install using Homebrew

```
brew install darksky-weather
```

![weather](screenshots/weather.png)

## Configuration

* The `update interval` of each component can be set by changing `update_cadence`. The unit is second.
