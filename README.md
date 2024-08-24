# hikvisionctl
cli tool for configurating hikvision cameras
# install
```sh
pip3 install https://github.com/jvmf1/hikvisionctl/archive/main.zip
```
# example
```sh
hikvisionctl -u admin -p password -i 192.168.0.10 --set-codec H.264
```
```sh
usage: hikvisionctl [-h] -u USER -p PASSWORD -i IP [--id ID] [--auth {digest,basic}] [--set-time-mode {NTP,manual}] [--set-localtime 2022-06-29T02:19:39+08:00]
                    [--set-timezone CST-8:00:00] [--set-ntp-server time.ntp.com] [--set-ntp-port 123] [--set-ntp-interval 1440] [--set-audio {true,false}]
                    [--set-audio-codec MP2L2] [--set-fps 3000] [--set-bitrate 1024] [--set-codec H.264] [--set-name name] [--set-device-number 123] [--set-smoothing 50]
                    [--set-quality 100] [--set-resolution 1920x1080] [--set-flashing {true,false}] [--set-transparent {true,false}] [--set-fontsize 16*16]
                    [--set-font-align alignLeft] [--set-overlay-name-enable {true,false}] [--set-overlay-name-position x,y] [--set-overlay-date-enable {true,false}]
                    [--set-overlay-date-position x,y] [--set-overlay-date-week {true,false}] [--set-overlay-date-format DD-MM-YYYY] [--set-overlay-date-style {12hour,24hour}]
                    [--set-overlay-1-text text] [--set-overlay-1-position x,y] [--set-overlay-1-enable {true,false}] [--reboot] [--list-time] [--list-online-users]
                    [--list-users] [--list-time-capabilities] [--list-channels] [--list-capabilities] [--list-deviceinfo] [--list-overlay] [--list-overlay-capabilities]

options:
  -h, --help            show this help message and exit
  -u USER, --user USER, --username USER
  -p PASSWORD, --password PASSWORD
  -i IP, --ip IP
  --id ID
  --auth {digest,basic}
  --set-time-mode {NTP,manual}
  --set-localtime 2022-06-29T02:19:39+08:00
  --set-timezone CST-8:00:00
  --set-ntp-server time.ntp.com
  --set-ntp-port 123
  --set-ntp-interval 1440
                        --list-time-capabilities to show all available options
  --set-audio {true,false}
  --set-audio-codec MP2L2
                        --list-capabilities to show all available options
  --set-fps 3000        --list-capabilities to show all available options
  --set-bitrate 1024    --list-capabilities to show all available options
  --set-codec H.264     --list-capabilities to show all available options
  --set-name name
  --set-device-number 123
  --set-smoothing 50    0-100
  --set-quality 100     --list-capabilities to show all available options
  --set-resolution 1920x1080
                        --list-capabilities to show all available options
  --set-flashing {true,false}
  --set-transparent {true,false}
  --set-fontsize 16*16  --list-overlay-capabilities to show all available options
  --set-font-align alignLeft
                        --list-overlay-capabilities to show all available options
  --set-overlay-name-enable {true,false}
  --set-overlay-name-position x,y
  --set-overlay-date-enable {true,false}
  --set-overlay-date-position x,y
  --set-overlay-date-week {true,false}
  --set-overlay-date-format DD-MM-YYYY
  --set-overlay-date-style {12hour,24hour}
  --set-overlay-1-text text
  --set-overlay-1-position x,y
  --set-overlay-1-enable {true,false}
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
