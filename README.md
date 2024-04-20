# Home Assistant for underfloor heating (Docker version) v2.0
Software (scripts) for Home Assistant in Docker.

I have used a Raspberry Pi 4B with the operating system [Raspberry Pi OS Lite (32-bit)](https://www.raspberrypi.com/software/operating-systems/). I have used an installation via the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).

There is the [installation of Docker Compose](https://dev.to/elalemanyo/how-to-install-docker-and-docker-compose-on-raspberry-pi-1mo). I use Home Assistant in [Container](https://www.home-assistant.io/installation/raspberrypi#docker-compose) (Docker Compose). 

- In a folder **HomeAssistant** is configuration for Home Assistant. It is necessary to copy content to a folder with the configuration Home Assistant.
- In a folder **AppDaemon** is configuration for [AppDaemon](https://appdaemon.readthedocs.io/en/latest/). I use AppDaemon in a container (Docker Compose). It is necessary to copy content to a folder with the configuration AppDaemon.
- In a folder **mosquitto** is configuration for [Mosquitto broker](https://mosquitto.org/). I use Mosquitto in a container (Docker Compose). It is necessary to copy content to a folder with configuration Mosquitto.

#### Tokens
It is necessary generate toke for [AppDaemon (appdaemon.yaml)](AppDaemon/appdaemon.yaml) and insert into part "token" and change url/IP address and the same token and url/IP address insert into [Docker compose settings for AppDaemon](docker_settings/compose.yml). The token for [bash script (ha_script.sh)](bash_scripts/ha_script.sh) and insert into part "token" and insert the same token into [bash script (script_bash.sh)](HomeAssistant/shell_command/script_bash.sh). These tokens are possible generate in GUI in the Home Assistant.

#### AppDaemon
- In [AppDaemon/apps/temperature_sensors.py](AppDaemon/apps/temperature_sensors.py) is necessary change ID sensors according to your IDs.
- In [AppDaemon/apps/thermoelectric_actuators_first_floor.py](AppDaemon/apps/thermoelectric_actuators_first_floor.py) and [AppDaemon/apps/thermoelectric_actuators_second_floor.py](AppDaemon/apps/thermoelectric_actuators_second_floor.py) is necessary change address boards according to your address.
- In [AppDaemon/apps/i2c_lcd.py](AppDaemon/apps/i2c_lcd.py) is necessary change address boards according to your address.


Settings for all containers are in a folder **docker_settings**.


More information at https://github.com/RomLab/system-for-underfloor-heating-v2.0
