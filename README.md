# hikvision-config
cli tool for configurating hikvision cameras
# example
```sh
./camera.py -u admin -p password -i 192.168.0.10 --set-codec H.264
```
```sh
usage: camera.py [-h] -u USER -p PASSWORD -i IP [--id ID] [--auth]
                 [--set-time-mode] [--set-localtime] [--set-timezone]
                 [--set-ntp-server] [--set-ntp-port] [--set-ntp-interval]
                 [--set-audio] [--set-audio-codec] [--set-fps] [--set-bitrate]
                 [--set-codec] [--set-name] [--set-device-number]
                 [--set-smoothing] [--set-quality] [--set-resolution]
                 [--set-flashing] [--set-transparent] [--set-fontsize]
                 [--set-font-align] [--set-overlay-name-enable]
                 [--set-overlay-name-position] [--set-overlay-date-enable]
                 [--set-overlay-date-position] [--set-overlay-date-week]
                 [--set-overlay-date-format] [--set-overlay-date-style]
                 [--set-overlay-1-text] [--set-overlay-1-position]
                 [--set-overlay-1-enable] [--reboot] [--list-time]
                 [--list-online-users] [--list-users]
                 [--list-time-capabilities] [--list-channels]
                 [--list-capabilities] [--list-deviceinfo] [--list-overlay]
                 [--list-overlay-capabilities]

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER, --username USER
  -p PASSWORD, --password PASSWORD
  -i IP, --ip IP
  --id ID
  --auth                digest | basic
  --set-time-mode       NTP | manual
  --set-localtime       2022-06-29T02:19:39+08:00
  --set-timezone        CST-8:00:00
  --set-ntp-server 
  --set-ntp-port 
  --set-ntp-interval 
  --set-audio           true | false
  --set-audio-codec 
  --set-fps 
  --set-bitrate 
  --set-codec 
  --set-name 
  --set-device-number 
  --set-smoothing 
  --set-quality 
  --set-resolution      1920x1080
  --set-flashing        true | false
  --set-transparent     true | false
  --set-fontsize 
  --set-font-align 
  --set-overlay-name-enable 
                        true | false
  --set-overlay-name-position 
                        x,y
  --set-overlay-date-enable 
                        true | false
  --set-overlay-date-position 
                        x,y
  --set-overlay-date-week 
                        true | false
  --set-overlay-date-format 
                        DD-MM-YYYY
  --set-overlay-date-style 
                        12hour | 24hour
  --set-overlay-1-text 
  --set-overlay-1-position 
                        x,y
  --set-overlay-1-enable 
                        true | false
  --reboot
  --list-time
  --list-online-users
  --list-users
  --list-time-capabilities
  --list-channels
  --list-capabilities
  --list-deviceinfo
  --list-overlay
  --list-overlay-capabilities

```
