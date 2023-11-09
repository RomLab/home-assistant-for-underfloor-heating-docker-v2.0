# Into root system: sudo apt-get install socat
# Add token into home/pi/bash_scripts/ha_script.sh and smb://192.168.11.196/home/pi/HomeAssistant/shell_command/script_bash.sh
# Add service as sudo: https://devicetests.com/crontab-reboot-not-working

[Unit]
Description=Run script at startup
After=network.target

[Service]
ExecStart=socat -u tcp-l:7777,fork system:/home/pi/bash_scripts/ha_script.sh
User=root
Group=root
Type=simple
Restart=on-failure

[Install]
WantedBy=multi-user.target
