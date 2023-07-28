# Home Assistant for underfloor heating (Docker version) v2.0
Software (scripts) for Home Assistant in Docker.

I have used a Raspberry Pi 4B with the operating system [Raspberry Pi OS Lite (32-bit)](https://www.raspberrypi.com/software/operating-systems/). I have used an installation via the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).

There is the [installation of Docker Compose](https://dev.to/elalemanyo/how-to-install-docker-and-docker-compose-on-raspberry-pi-1mo). I use Home Assistant in [Container](https://www.home-assistant.io/installation/raspberrypi#docker-compose) (Docker Compose). 

- In a folder **HomeAssistant** is configuration for Home Assistant. It is necessary to copy content to a folder with the configuration Home Assistant.
- In a folder **AppDaemon** is configuration for [AppDaemon](https://appdaemon.readthedocs.io/en/latest/). I use AppDaemon in a container (Docker Compose). It is necessary to copy content to a folder with the configuration AppDaemon.
- In a folder **mosquitto** is configuration for [Mosquitto broker](https://mosquitto.org/). I use Mosquitto in a container (Docker Compose). It is necessary to copy content to a folder with configuration Mosquitto.

Settings for all containers are in a folder **docker_settings**.


More information at https://github.com/RomLab/system-for-underfloor-heating-v2.0
