#!/bin/bash
read message

token=""
scriptDirectory=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
nameOfLogFile="${scriptDirectory}/rpi_commands_log.txt"
dateAndTime=$(date '+%d-%m-%Y %H:%M:%S')

case $message in

  "ha_shutdown_${token}")
    echo -n "Shutdown RPI"
    echo "${dateAndTime}: Shutdown RPI" >> $nameOfLogFile
    shutdown -h now
    ;;

  "ha_reboot_${token}")
    echo -n "Reboot RPI"
    echo "${dateAndTime}: Reboot RPI" >> $nameOfLogFile
    shutdown -r now
    ;;

  *)
    echo "Bad input command"
    echo "${dateAndTime}: Bad input command: ${message}" >> $nameOfLogFile
    ;;
esac
