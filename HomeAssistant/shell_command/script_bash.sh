#!/bin/bash
token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmODk2OTljYmM0NjQ0YTc3YWM4MTgwN2M5Mzc1YTE3MSIsImlhdCI6MTY5NDYzNDY4NiwiZXhwIjoyMDA5OTk0Njg2fQ.MLKnVs0Qjj27lFRdXdN6DZmoLidduHGhe3NWRVFd9-A"
# Gets input parameter
parameter=$1
# Gets IP4 address
ipAddress=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)

case $parameter in 

  "ha_shutdown")
    echo "ha_shutdown_${token}" | nc $ipAddress 7777
    ;;

  "ha_reboot")
    echo "ha_reboot_${token}" | nc $ipAddress 7777
    ;;

  *)
    return 1
    ;;
esac
