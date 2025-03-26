#                                                                                                                                                         #
#                                                                                                                                                         #
#               ▄▄▄█████▓ ██░ ██  ██▀███   ▒█████   ▄▄▄     ▄▄▄█████▓    ▄████▄   █    ██ ▄▄▄█████▓▄▄▄█████▓▓█████  ██▀███                                #
#               ▓  ██▒ ▓▒▓██░ ██▒▓██ ▒ ██▒▒██▒  ██▒▒████▄   ▓  ██▒ ▓▒   ▒██▀ ▀█   ██  ▓██▒▓  ██▒ ▓▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒                              #
#               ▒ ▓██░ ▒░▒██▀▀██░▓██ ░▄█ ▒▒██░  ██▒▒██  ▀█▄ ▒ ▓██░ ▒░   ▒▓█    ▄ ▓██  ▒██░▒ ▓██░ ▒░▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒                              #                           #
#               ░ ▓██▓ ░ ░▓█ ░██ ▒██▀▀█▄  ▒██   ██░░██▄▄▄▄██░ ▓██▓ ░    ▒▓▓▄ ▄██▒▓▓█  ░██░░ ▓██▓ ░ ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄                                #
#                 ▒██▒ ░ ░▓█▒░██▓░██▓ ▒██▒░ ████▓▒░ ▓█   ▓██▒ ▒██▒ ░    ▒ ▓███▀ ░▒▒█████▓   ▒██▒ ░   ▒██▒ ░ ░▒████▒░██▓ ▒██▒                              #
#                 ▒ ░░    ▒ ░░▒░▒░ ▒▓ ░▒▓░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒ ░░      ░ ░▒ ▒  ░░▒▓▒ ▒ ▒   ▒ ░░     ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░                              #
#                   ░     ▒ ░▒░ ░  ░▒ ░ ▒░  ░ ▒ ▒░   ▒   ▒▒ ░   ░         ░  ▒   ░░▒░ ░ ░     ░        ░     ░ ░  ░  ░▒ ░ ▒░                              #
#                 ░       ░  ░░ ░  ░░   ░ ░ ░ ░ ▒    ░   ▒    ░         ░         ░░░ ░ ░   ░        ░         ░     ░░   ░                               #                       #
#                         ░  ░  ░   ░         ░ ░        ░  ░           ░ ░         ░                          ░  ░   ░                                   #
#                                                                                                                                                         #
# ======================================================================================================================================================= #
#                                                                                                                                                         #
#      This is a program to monitor the internet connection.                                                                                              # 
#      The tester will consist of the following items:                                                                                                    #
#                                                                                                                                                         #
#            RasPi Pico                                                                                                                                   #
#            128x32 Oled display                                                                                                                          #
#            2 relays to switch power to Modem and Router                                                                                                 #
#            Led Indicator/s                                                                                                                              #
#            Pushbutton switches x 2                                                                                                                      #
#                                                                                                                                                         #
# Design notes:                                                                                                                                           # 
#       make the boot wait time approx 1 minute                                                                                                           # 
#                                                                                                                                                         #       
#                                                                                                                                                         #
#       a switch sets the Mode. Modes are:   Reboot Modem :   The associated relay switches off and beeps, then on.                                       #
#                                            Reboot Router:   The associated relay switches off and beeps, then on.                                       #
#                                            Auto         :   The internet is connected and monitored                                                     #
#                                                             The internet is booting - no activity                                                       #
#                                                             The internet is waiting for SSID response, but not yet connected                            #
#       buzzer beeps when internet is depowered                                                                                                           # 
#       buzzer tweeps when internet is repowered                                                                                                          # 
#       a LCD displays relevant info                                                                                                                      # 
#                                                                                                                                                         #
#       The device will operate in the following manner:                                                                                                  #
#           The device turns on the relays to power the modem and router display a sign-on on the lcd     LCD message #1                                  #
#           The device will wait for 20 seconds                                                                                                           #
#           The device will try to the WLAN, router and a network device                                                                                  #
#           When it connects, it will give a LCD message.                                                                                                 # 
#           Pings will occur every 30 seconds to ensure connection                                                                                        #
#           If it loses connection, it will wait 30 seconds to try again twice                                                                            #
#           After 3 retrys, it will disconnect power for 3 seconds, then go throught the power-up sequence                                                #
#           The addresses pinged are:                                                                                                                     #
#               WLAN      :  1.1.1.1       (Cloud Flare)            Green                                                                                 #
#               LAN       :  192.168.1.254 (Router address)         Red                                                                                   #
#               Network   :  192.168.1.70  (PiHole)                 Blue                                                                                  #
#                                                                                                                                                         #
# ======================================================================================================================================================= #
#                                                                                                                                                         #
# 08-Mar-2025               Version : 1.0     Intital boxing                                                                                              #
# 09-Mar-2025               Version : 1.1     Removed w'dog. Changed time printout for friendlier version                                                 #
# 10-Mar-2025               Version : 1.2     Added neopixel operation                                                                                    #
# 13-Mar-2025               Version : 1.3     Added SD card w/r                                                                                           #
# 16-Mar-2025               Version : 1.4     Cleaned up everything. Fingers crossed                                                                      #
# 23-Mar-2025               Version : 1.5     Added W'dog back in.                                                                                        #
# 26-Mar-2025               Version : 1.6     Added OTA Updates                                                                                           #
#                                                                                                                                                         #
# Stitching and butchery done by Tony Flynn. Try not to snigger                                                                                           #
#                                                                                                                                                         #
#=========================================================================================================================================================#
PROG_NAME = "Throat Cutter"
CURR_VER  = "Version 1.6"
CURR_DATE = "26-Mar-25"
# https://gist.github.com/shawwwn/91cc8979e33e82af6d99ec34c38195fb
# µPing (MicroPing) for MicroPython
# copyright (c) 2018 Shawwwn <shawwwn1@gmail.com>
# License: MIT

# Internet Checksum Algorithm
# Author: Olav Morken
# https://github.com/olavmrk/python-ping/blob/master/ping.py
# @data: bytes
def checksum(data):
    if len(data) & 0x1: # Odd number of bytes
        data += b'\0'
    cs = 0
    for pos in range(0, len(data), 2):
        b1 = data[pos]
        b2 = data[pos + 1]
        cs += (b1 << 8) + b2
    while cs >= 0x10000:
        cs = (cs & 0xffff) + (cs >> 16)
    cs = ~cs & 0xffff
    return cs

def ping(host, count=4, timeout=5000, interval=10, quiet=False, size=64):
    import utime
    import uselect
    import uctypes
    import usocket
    import ustruct
    import urandom
    import network

    # prepare packet
    assert size >= 16, "pkt size too small"
    pkt = b'Q'*size
    pkt_desc = {
        "type": uctypes.UINT8 | 0,
        "code": uctypes.UINT8 | 1,
        "checksum": uctypes.UINT16 | 2,
        "id": uctypes.UINT16 | 4,
        "seq": uctypes.INT16 | 6,
        "timestamp": uctypes.UINT64 | 8,
    } # packet header descriptor
    h = uctypes.struct(uctypes.addressof(pkt), pkt_desc, uctypes.BIG_ENDIAN)
    h.type = 8 # ICMP_ECHO_REQUEST
    h.code = 0
    h.checksum = 0
    h.id = urandom.getrandbits(16)
    h.seq = 1

    # init socket
    sock = usocket.socket(usocket.AF_INET, usocket.SOCK_RAW, 1)
    sock.setblocking(0)
    sock.settimeout(timeout/1000)
    addr = usocket.getaddrinfo(host, 1)[0][-1][0] # ip address
    sock.connect((addr, 1))
    not quiet and print("PING %s (%s): %u data bytes" % (host, addr, len(pkt)))

    seqs = list(range(1, count+1)) # [1,2,...,count]
    c = 1
    t = 0
    n_trans = 0
    n_recv = 0
    finish = False
    while t < timeout:
        if t==interval and c<=count:
            # send packet
            h.checksum = 0
            h.seq = c
            h.timestamp = utime.ticks_us()
            h.checksum = checksum(pkt)
            if sock.send(pkt) == size:
                n_trans += 1
                t = 0 # reset timeout
            else:
                seqs.remove(c)
            c += 1

        # recv packet
        while 1:
            socks, _, _ = uselect.select([sock], [], [], 0)
            if socks:
                resp = socks[0].recv(4096)
                resp_mv = memoryview(resp)
                h2 = uctypes.struct(uctypes.addressof(resp_mv[20:]), pkt_desc, uctypes.BIG_ENDIAN)
                # TODO: validate checksum (optional)
                seq = h2.seq
                if h2.type==0 and h2.id==h.id and (seq in seqs): # 0: ICMP_ECHO_REPLY
                    t_elasped = (utime.ticks_us()-h2.timestamp) / 1000
                    ttl = ustruct.unpack('!B', resp_mv[8:9])[0] # time-to-live
                    n_recv += 1
                    not quiet and print("%u bytes from %s: icmp_seq=%u, ttl=%u, time=%f ms" % (len(resp), addr, seq, ttl, t_elasped))
                    seqs.remove(seq)
                    if len(seqs) == 0:
                        finish = True
                        break
            else:
                break

        if finish:
            break

        utime.sleep_ms(1)
        t += 1

    # close
    sock.close()
    ret = (n_trans, n_recv)
    not quiet and print("%u packets transmitted, %u packets received" % (n_trans, n_recv))
    return (n_trans, n_recv)

"""
Framework Copyright (c) 2024 Gary Sims
MIT License

"""

from time import sleep
import network
import time
from machine import Pin, RTC, SPI, WDT
from PiicoDev_SSD1306 import *
import rp2
import sys
import utime
import usocket
import ustruct
import neopixel
import sdcard
import uos
from utime import sleep_ms
from ota import OTAUpdater
from WiFi_config import mySSID, myPASSWORD

interval     = 29                                                         #time between tests (was 180)
attempt_conn = 0
WLAN_COUNT   = 0
ROUTE_COUNT  = 0
NAS_COUNT    = 0
modem_died   = 0
router_died  = 0
both_died    = 0

np_color     = ""


# Initialize Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm=0xa11140)                                              # Prevent idle mode
    rp2.country('AU')                                                     # Set your country code
#    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    wlan.connect(mySSID, myPASSWORD)

    max_wait = 10
    attempt_conn = 0
    MAX_WAIT_OLD = max_wait

    if wlan.status() != 3:
        print("Waiting for connection...")
    while max_wait > 0:
        if max_wait != MAX_WAIT_OLD or max_wait < 0:
            wdt.feed()                                                    # Reset the watchdog timer
            print("mw= ",max_wait," - MWO= ", MAX_WAIT_OLD)
            MAX_WAIT_OLD = max_wait
            
        attempt_conn += 1       
        np[0] = (RED_V, 0, BLUE_V)                                        # Update NeoPixel LED Magenta
        np.write()
        sleep_ms(250)

        # Display connection status
        display.fill(0)
        display.text("Waiting to", 25, 15, 1)
        display.text("connect", 35, 30, 1)
        display.text(str(attempt_conn), 62, 45, 1)
        display.show()

        # Check connection status
        if wlan.status() < 0 or wlan.status() >= 3:
#            print("WLAN status:", wlan.status())
            np[0] = (RED_V, GREEN_V, BLUE_V)                              # White
            np.write()
            sleep_ms(10)
            break
        max_wait -= 1
        sleep(1)

    if wlan.status() != 3:
        log_event("Connection failed", wlan.status())
        print("Connection failed - status ", wlan.status())
        
        return None
    else:
        attempt_conn = 0
        if WIFI_FLAG == False:
            print("Connected successfully!")
            print("IP address:", wlan.ifconfig()[0])
            wdt.feed()                                                   # Reset the watchdog timer
            
        return wlan

# Log events to a CSV file
def log_event(event, status):
    try:
        if WIFI_FLAG == False:
            with open("/sd/event_log.csv", "a") as file:
                file.write(f"{SeqNo},\"WiFi code : {status}\",\"{date}\",\"{time}\"\n")
    except Exception as e:
        print("Failed to write to log:", e)
  
# Monitor Wi-Fi connection dynamically
def monitor_wifi():
    wlan = connect_to_wifi()
    while True:
        if wlan and wlan.status() == 3:                                     # If connected
            status = wlan.ifconfig()
            global WIFI_FLAG
            if WIFI_FLAG == False:
                display.fill(0)
                display.text('IP Address:', 25, 15, 1)
                display.text(status[0], 17, 30, 1)
                display.text("WiFi is on", 25, 45, 1)
                display.show()
            WIFI_FLAG = True
            np[0] = (0, GREEN_V, 0)                                          # Green LED
            np.write()
            sleep_ms(10)
        else:
            log_event("Connection lost", wlan.status() if wlan else "WLAN WiFi unstable")
            print("Connection lost, attempting to reconnect...")
            wlan = connect_to_wifi()
            WIFI_FLAG = False
            
        break
#        sleep(30)                                                           # Monitor every 30 seconds

# Determine the GMT offset for Melbourne dynamically
def get_gmt_offset():
    # Define offsets
    AEST_OFFSET = 3600 * 10  # UTC+10
    AEDT_OFFSET = 3600 * 11  # UTC+11

    # Determine if it's daylight saving time (DST)
    current_time = utime.localtime()
    month = current_time[1]
    day = current_time[2]

    # DST in Melbourne typically starts in October and ends in April
    if (month > 10 or (month == 10 and day >= 1)) or (month < 4 or (month == 4 and day <= 7)):
        return AEDT_OFFSET  # Summer (AEDT)
    else:
        return AEST_OFFSET  # Winter (AEST)

def getTimeNTP():
    NTP_DELTA = 2208988800
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    try:
        addr = usocket.getaddrinfo(NTP_HOST, 123)[0][-1]
        s = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
        try:
            s.settimeout(1)
            res = s.sendto(NTP_QUERY, addr)
            msg = s.recv(48)
        finally:
            s.close()
        ntp_time = ustruct.unpack("!I", msg[40:44])[0]
        return utime.gmtime(ntp_time - NTP_DELTA + GMT_OFFSET)
    except Exception as e:
        print("NTP error:", e)
        # Return current RTC time as fallback
        return utime.localtime()

# Function: copy time to PI Pico's RTC
def setTimeRTC():
    tm = getTimeNTP()
    rtc.datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

# Function: format date and time
def format_datetime(rtc):
    # Retrieve current RTC time
    now = rtc.datetime()

    # Extract components
    year, month, day, _, hour, minute, second, _ = now

    # Month names
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_string = month_names[month - 1]

    # Format date as "3-Apr-2025"
    date_string = f"{day}-{month_string}-{year}"

    # Format time as "18:35:27"
    time_string = f"{hour:02}:{minute:02}:{second:02}"

    return date_string, time_string


def zero_counters():
    global WLAN_COUNT
    WLAN_COUNT   = 0
    global ROUTE_COUNT
    ROUTE_COUNT  = 0
    global NAS_COUNT
    NAS_COUNT    = 0

def test_by_ping(host, ledok):
    wdt.feed()                                                                 # Reset the watchdog timer
    try:
        ping_sent, ping_recv = ping(host, quiet=True)
        ledok.off()
        if ping_sent > 0 and ping_recv > 0:
            ledok.on()
        else:
            ledok.off()
    except Exception as e:
        print(f"Ping error to {host}: {e}")
        ledok.off()        
               
def reboot_devices():
    print('Powering up devices')
    date, time = format_datetime(rtc) 
    if SD_ERROR == False:
        global SeqNo                                                           # Declare global at the beginning
        with open("/sd/event_log.csv", "a") as file:
            file.write(f"{SeqNo},\"Power Up Modem & Router\",\"{date}\",\"{time}\"\n")
            SeqNo += 1
            save_variables(SeqNo)
    RLY_1.on()                                                                 #power up the Modem and Router    
    RLY_2.on()
    site1ok.off()
    site2ok.off()
    site3ok.off()
    init_countdown = 40                                                        #20 seconds
    countdown_passes = 0

    while init_countdown > 0:
        init_countdown -= 1
        countdown_passes += 1        
        display.fill(0)
        display.text("Power up",33,15, 1)
        display.text("Sequence",33, 30, 1)
        display.text("Initialised",23, 45, 1)
        if (init_countdown % 2) == 0:
            wdt.feed()                                                        # Reset the watchdog timer
            ledi.toggle()                                                     #Flash the led on the Pico
            np[0] = (0, 0, BLUE_V)                                            # Set the neopixel LED to blue. RGB values
            np.write()                                                        # Update the LED
            sleep_ms(10)
#             wdt.feed()                                                        #Feed the watchdog
            display.text("*",120,5, 1)
            display.text(" ",10,5,1)
        else:
            np[0] = (0, 0, 0)                                                 # toggle the neopixel LED off
            np.write()                                                        # Update the LED
            sleep_ms(10)
            display.text("*",10,5, 1)
            display.text(" ",120,5, 1)
        display.show()
        if init_countdown == 3 or countdown_passes == 1:
            display.text("-+-",62, 55, 1)
            display.show
        if init_countdown == 2 or countdown_passes == 2:
            BUZZ.on()
            sleep_ms(15)
            BUZZ.off()
        sleep_ms(485)
    print("reset counters")
    zero_counters()
    print("waiting...")
    display.fill(0)
    display.text("Waiting...",33, 30, 1)
    display.show
    np[0] = (0, 0, 0)                                                         # toggle the neopixel LED off
    np.write()                                                                # Update the LED
    sleep_ms(10)
    check_sd_card()                                                           # Check if the SD card is fitted
        
def disconnect_modem():
    print('De-powering modem')
    date, time = format_datetime(rtc) 
    if SD_ERROR == False:
        global SeqNo
        with open("/sd/event_log.csv", "a") as file:
            file.write(f"{SeqNo},\"Depower Modem\",\"{date}\",\"{time}\"\n")
            SeqNo += 1
            save_variables(SeqNo)
    RLY_1.off()                                                               # power down the Modem
    np[0] = (RED_V, 0, 0)                                                     # Set the neopixel LED to red. RGB values
    np.write()                                                                # Update the LED
    sleep_ms(10)
    display.fill(0)
    display.text("Modem ",43,15, 1)
    display.text("power down",30,30, 1)
    display.show()
    global modem_died
    modem_died += 1
    three_beeps()
    reboot_devices()
    
def disconnect_router():
    print('De-powering router')
    date, time = format_datetime(rtc) 
    if SD_ERROR == False:
        global SeqNo
        with open("/sd/event_log.csv", "a") as file:
            file.write(f"{SeqNo},\"Depower Router\",\"{date}\",\"{time}\"\n")
            SeqNo += 1
            save_variables(SeqNo)
    RLY_2.off()                                                               # power down the Router
    np[0] = (RED_V, GREEN_V, 0)                                               # Set the neopixel LED to yellow. RGB values
    np.write()                                                                # Update the LED
    sleep_ms(10)
    display.fill(0)
    display.text("Router",43,15, 1)
    display.text("power down",30,30, 1)
    display.show()
    global router_died
    router_died += 1
    three_beeps()
    reboot_devices()
    
def disconnect_both():
    print('De-powering All')
    date, time = format_datetime(rtc) 
    if SD_ERROR == False:
        global SeqNo
        with open("/sd/event_log.csv", "a") as file:
            file.write(f"{SeqNo},\"Depower All\",\"{date}\",\"{time}\"\n")
            SeqNo += 1
            save_variables(SeqNo)
    RLY_1.off()                                                               # power down the Modem & Router
    RLY_2.off()
    np[0] = (0, GREEN_V, BLUE_V)                                              # Set the neopixel LED to cyan. RGB values
    np.write()                                                                # Update the LED
    sleep_ms(10)
    display.fill(0)
    display.text("Modem & Router",20,15, 1)
    display.text("power down",30,30, 1)
    display.show()
    global both_died
    both_died += 1
    three_beeps()
    reboot_devices()
    
def three_beeps():
    times = 3
    ledi.toggle()                                                             #Flash the led on the Pico
#     wdt.feed()                                                                #Feed the watchdog
    while times > 0:
        times -= 1
        BUZZ.on()
        sleep_ms(15)
        BUZZ.off()
        sleep_ms(985)

def check_sd_card():
    global SD_ERROR                                                           # Allow modification of the global SD_ERROR variable
    try:        
        uos.stat("/sd")                                                       # Use uos.stat() to check if the '/sd' directory exists
#        print("SD card detected.")
        SD_ERROR = False                                                      # Reset SD_ERROR if SD card is found
    except OSError:
        print("WARNING: SD card not detected.")
        SD_ERROR = True                                                       # Set SD_ERROR if SD card is not found

def check_csv():                                                              # Check if CSV file exists; if not, create it with a header
    try:                                                                      # Try to check if the file exists
        uos.stat(file_path)
    except OSError:                                                           # If an error is raised, the file does not exist
        print("File does not exist. Creating file...")
        with open(file_path, 'w') as file:
            file.write('SeqNo,Event,Datestamp,Timestamp\n')
            print("File created with header.")

def save_variables(SeqNo):
    with open(VARIABLES_PATH, "w") as file:
        file.write(f"{SeqNo}\n")

def load_variables():
    try:
        with open("variables.txt", "r") as file:
            lines = file.readlines()
            SeqNo = int(lines[0].strip())
            return SeqNo
    except OSError:
        print("No saved variables found.")
        return 0                                                              # Default values if no file exists

# Time shit
rtc = machine.RTC()                                                           # Initialize the RTC (Real-Time Clock)
GMT_OFFSET     = get_gmt_offset()                                             # Set the GMT offset
NTP_HOST       = 'pool.ntp.org'                                               # NTP-Host

# WIFI_SSID      = 'missus'
# WIFI_PASSWORD  = 'network+key'
WIFI_FLAG      = False

firmware_url = "https://github.com/LookMum-NoHands/Throat-Cutter/tree/main/Code"
ota_updater = OTAUpdater(mySSID, myPASSWORD, firmware_url, "main.py")

VARIABLES_PATH = "variables.txt"                                              # In root filesystem


wdt = WDT(timeout=6000)                                                       #set for 6 seconds

# Led definitions
led_green  = Pin(18, Pin.OUT, value=0)                                        # OK mode            // Router Reboot
led_red    = Pin(19, Pin.OUT, value=0)                                        # Modem Reboot
led_blue   = Pin(20, Pin.OUT, value=0)                                        # Initialising mode  // Router Reboot

# Relay ouput definitions
RLY_1      = Pin(12, Pin.OUT, value=0)                                        # Modem 
RLY_2      = Pin(11, Pin.OUT, value=0)                                        # Router

# Switch definitions
SW_MODEM   = Pin(14, Pin.IN, Pin.PULL_UP)                                     # Reboot Modem
SW_ROUTER  = Pin(15, Pin.IN, Pin.PULL_UP)                                     # Reboot Router

# Diagnostics
BUZZ       = Pin(16, Pin.OUT, value=0)                                        # air raid siren whoop whoop machine

# Define the GPIO pin and number of LEDs
pin = machine.Pin(13)                                                         # Neopixel GPIO pin
num_leds = 1                                                                  # LEDs to drive
np = neopixel.NeoPixel(pin, num_leds)
RED_V    = 24                                                                 # Red intensity (0-256)
GREEN_V  = 24                                                                 # Green intensity (0-256)
BLUE_V   = 24                                                                 # Blue intensity (0-256)

ota_count = 0                                                                 # iterations until Over-The-Air checked

# Oled
display = create_PiicoDev_SSD1306()                                           # Sets the I2C up. note address of LCD is 0x3C

# Assign chip select (CS) pin and start it high
cs = machine.Pin(5, machine.Pin.OUT)

# Initialise SPI peripheral - start with 1MHz
spi = machine.SPI(0,
                  baudrate = 1300000,
                  polarity = 0,
                  phase = 0,
                  bits = 8,
                  firstbit = machine.SPI.MSB,
                  sck = machine.Pin(6),
                  mosi = machine.Pin(7),
                  miso = machine.Pin(4))

sd = sdcard.SDCard(spi, cs)                                                   # Initialise the SD card

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")
file_path = "/sd/event_log.csv"

SD_ERROR = False                                                                  # Initialise the SD error flag
check_sd_card()                                                               # Call the function to check SD card status

if SD_ERROR == False:
    check_csv()

# read_last_seq_no()
SeqNo = load_variables()
print("SeqNo is ", SeqNo)

ledi = Pin("LED", Pin.OUT)
ledi.off()

site1 = "1.1.1.1"           #Wibbly Wobbly Web
site1ok = Pin(18, Pin.OUT)  #green
site1ok.on()
site1bad = WLAN_COUNT

site2 = "192.168.1.254"     #Billion Router
site2ok = Pin(19, Pin.OUT)  #red
site2ok.on()
site2bad = ROUTE_COUNT

site3 = "192.168.1.70"      #PiHole
site3ok = Pin(20, Pin.OUT)  #blue
site3ok.on()
site3bad = NAS_COUNT

ledi.on()
site1ok.off()
site2ok.off()
site3ok.off()

# Initialize date and time variables before they might be used
date, time = "", ""
try:
    date, time = format_datetime(rtc)
except Exception as e:
    print("Error getting date/time:", e)
    
if SD_ERROR == False:
    with open("/sd/event_log.csv", "a") as file:
        file.write(f"{SeqNo},\"A cow is born\",\"{date}\",\"{time}\"\n")
        SeqNo += 1
        save_variables(SeqNo)

reboot_devices()

monitor_wifi()

print("Returned from WLAN")

sleep(2)
wdt.feed()                                                                      # Reset the watchdog timer
rtc = RTC()
setTimeRTC()                                                                    # Set the time

date, time = format_datetime(rtc)                                               # Get the current time & date
print(f"Date: {date}")
print(f"Time: {time}")
if SD_ERROR == False:
    with open("/sd/event_log.csv", "a") as file:
        file.write(f"{SeqNo},\"Wlan Connected\",\"{date}\",\"{time}\"\n")
        SeqNo += 1
        save_variables(SeqNo) 

# print(rtc.datetime())
display.fill(0)
display.show()
sleep_ms(250)
display.fill(0)
display.text("Time is set", 20, 15, 1)
display.text(f"{date}", 20, 30, 1)
display.text(f"{time}", 32, 45, 1)
display.show()
sleep(3)
wdt.feed()                                                                      # Reset the watchdog timer

# Create a file and write equipment information to it
if SD_ERROR == False:
    with open("/sd/Read_info.txt", "w") as file:
        file.write(str(PROG_NAME) + "\r\n")
        file.write(str(CURR_DATE) + "\r\n")
        file.write(str(CURR_VER) + "\r\n")
        sleep(1)
   
c = interval
while True:
    ledi.toggle()                                                               #Flash the led on the Pico
    sleep_ms(1)
    wdt.feed()                                                                  # Reset the watchdog timer
    np[0] = (0, GREEN_V, 0)                                                     # Set the neopixel LED to green. RGB values
    np.write()                                                                  # Update the LED
    np[0] = (0, GREEN_V, 0)                                                     # Set the neopixel LED to green. RGB values
    np.write()                                                                  # Update the LED
    sleep_ms(10)

# Test for OTA activation
    ota_count =+ 1
    if ota_count => 480:                                                        # 120 per hour = 4 hours
        ota_updater.download_and_install_update_if_available()                  # do the ota check magic here

#    wdt.feed()                                                                    #Feed the watchdog
    
    if WLAN_COUNT == 0 and ROUTE_COUNT == 0 and NAS_COUNT == 0:
        display.fill(0)
        display.text("'Net is on", 30, 20, 1)
        display.text("Wifi is on", 30, 40, 1)
        display.show()
        
    else:
        display.fill(0)
        display.text("Error detected", 15, 15, 1)
        display.text("Don't panic", 30, 30, 1)
        display.text("..... yet", 35, 45, 1)
        display.show()        
    
    if SW_MODEM.value() == 0:                                                  # if the modem SW2 is pressed
        date, time = format_datetime(rtc)                                      # get the current time
        if SD_ERROR == False:
            with open("/sd/event_log.csv", "a") as file:
                file.write(f"{SeqNo},\"Modem Switch Pressed\",\"{date}\",\"{time}\"\n")
                SeqNo += 1
                save_variables(SeqNo)
        disconnect_modem()
        
    if SW_ROUTER.value() == 0:                                                 # if the router SW1 is pressed
        date, time = format_datetime(rtc) 
        if SD_ERROR == False:
            with open("/sd/event_log.csv", "a") as file:
                file.write(f"{SeqNo},\"Router Switch Pressed\",\"{date}\",\"{time}\"\n")
                SeqNo += 1
                save_variables(SeqNo)
        disconnect_router()

    c = c + 1
    display.text(str(c), 62, 5, 1)
    display.show()
    np[0] = (0, GREEN_V, 0)                                                     # Set the neopixel LED to green. RGB values
    np.write()
    np[0] = (0, GREEN_V, 0)                                                     # Set the neopixel LED to green. RGB values
    np.write()
    sleep_ms(10)
    if c >= interval:
        np[0] = (0, GREEN_V, 0)                                                 # Set the neopixel LED to green. RGB values
        np.write()                                                              # Update the LED
        sleep_ms(10)
        display.text(str(c), 62, 5, 1)
        display.show()
        test_by_ping(site1, site1ok)
        display.text("1", 30, 55, 1)
        display.show()
        print("WLAN IP OK - ", end="")
        test_by_ping(site2, site2ok)
        display.text("2", 64, 55, 1)
        display.show()
        print("ROUTER IP OK - ", end="")
        test_by_ping(site3, site3ok)
        display.text("3", 100, 55, 1)
        display.show()
        print("NAS IP OK")
        wdt.feed()                                                              # Reset the w'dog
        if site1ok.value() == False:
            WLAN_COUNT += 1
            display.text("", 30, 20, 1)
            display.show()
            np[0] = (RED_V, 0, 0)                                               # Set the neopixel LED to red. RGB values
            np.write()
            sleep_ms(10)
            date, time = format_datetime(rtc) 
            if SD_ERROR == False:
                with open("/sd/event_log.csv", "a") as file:
                    file.write(f"{SeqNo},\"Failure - WLAN error {WLAN_COUNT}\",\"{date}\",\"{time}\"\n")
                    SeqNo += 1
                    save_variables(SeqNo)
        else:
            WLAN_COUNT = 0
            
        if site2ok.value() == False:
            display.text("", 30, 40, 1)
            display.show()
            ROUTE_COUNT += 1
            np[0] = (RED_V, GREEN_V, 0)                                         # Set the neopixel LED to yellow. 
            np.write()
            sleep_ms(10)
            date, time = format_datetime(rtc) 
            if SD_ERROR == False:
                with open("/sd/event_log.csv", "a") as file:
                    file.write(f"{SeqNo},\"Failure - Router error {ROUTE_COUNT} \",\"{date}\",\"{time}\"\n")
                    SeqNo += 1
                    save_variables(SeqNo)
        else:
            ROUTE_COUNT = 0
            
        if site3ok.value() == False:
            display.text("", 30, 40, 1)
            display.show()
            NAS_COUNT += 1
            np[0] = (RED_V, GREEN_V, 0)                                         # Set the neopixel LED to yellow
            np.write()                                                          # Update the LED
            sleep_ms(10)
            date, time = format_datetime(rtc) 
            if SD_ERROR == False:
                with open("/sd/event_log.csv", "a") as file:
                    file.write(f"{SeqNo},\"Failure - NAS/LAN error {NAS_COUNT} \",\"{date}\",\"{time}\"\n")
                    SeqNo += 1
                    save_variables(SeqNo)
        else:
            NAS_COUNT = 0
            
        print("W",WLAN_COUNT, " - R",ROUTE_COUNT, " - N",NAS_COUNT, "   Modem -",modem_died, "  Router -",router_died, "  Both -",both_died)
        c = 0
        
        if WLAN_COUNT >= 3 and (ROUTE_COUNT >= 3 or NAS_COUNT >= 3):
            print('The Nuclear Option has been selected')
            disconnect_both()
            reboot_devices()
            zero_counters()

        if WLAN_COUNT >= 3:
            print('DefCon 3 has been selected')
            disconnect_modem()
            reboot_devices()
            zero_counters()

        if  ROUTE_COUNT >= 3 or NAS_COUNT >= 3:    
            print('Kiss the Router goodbye')
            disconnect_router()
            reboot_devices()
            zero_counters()
            
        monitor_wifi()

    sleep(1)
    
