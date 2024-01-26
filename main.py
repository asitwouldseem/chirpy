## TTS courtesy TTSMaker. Voice 148 (Alayna US). https://ttsmaker.com/
## Cat Meow courtesy bagenzo. CC0. https://freesound.org/people/bagenzo/sounds/714179/

import machine
import utime
import urandom
from machine import Pin
from picodfplayer import DFPlayer

# Setup UART connection with DFPlayer
UART_INSTANCE = 0
TX_PIN = 16
RX_PIN = 17
BUSY_PIN = 22

# Other constants
DEFAULT_VOLUME = 20
INTERVAL_START = 5
INTERVAL_END = 25

# Setup I/O
player = DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
device_armed = False

def meow():
    # Generate random duration, and sleep device.
    interval = urandom.randint(INTERVAL_START, INTERVAL_END)
    print(interval)

    utime.sleep(interval)
    
    player.playTrack(1,1)

    # Eh, I hate this. But works for now.
    if button.value():
        print("Button pressed")
        user_input()

def user_input():
    global device_armed
    
    device_armed = not device_armed
    
    # Device armed.
    while device_armed == True:
        player.playTrack(2,1)
        meow()
    
    # Device disarmed.
    if device_armed == False:
        player.playTrack(2,2)

def init():    
    player.setVolume(DEFAULT_VOLUME)
    
    main()
    
def main():
    while True:
        if button.value():
            print("Button pressed")
            user_input()

        utime.sleep(1)

init()
