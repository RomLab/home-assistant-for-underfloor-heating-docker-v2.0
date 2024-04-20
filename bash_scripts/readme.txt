# Into root system: sudo apt-get install socat

# Create a token with name bash_script_control_rpi (in the Home Assistant --> Name --> Long-Lived Access Tokens --> CreateToken) and paste the token into 
# home/pi/bash_scripts/ha_script.sh and smb://[Your IP address]/home/pi/HomeAssistant/shell_command/script_bash.sh

# Add service:
# cd /lib/systemd/system
# sudo touch homeassistantcontrolrpi.service
# sudo nano homeassistantcontrolrpi.service
# Copy service below to the new service file.
# sudo systemctl daemon-reload
# sudo systemctl enable homeassistantcontrolrpi.service
# sudo systemctl start homeassistantcontrolrpi.service 
# Control status service: sudo systemctl status homeassistantcontrolrpi.service 


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
