import RPi.GPIO as GPIO
import time

# -----------------------------
# GPIO SETUP
# -----------------------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

BLUE_LED = 29   # Clear weather LED
PINK_LED = 31   # Rain / severe weather LED

GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(PINK_LED, GPIO.OUT)

# -----------------------------
# BASE STATES
# -----------------------------
def idle_weather():
    """Both LEDs ON, no blinking"""
    GPIO.output(BLUE_LED, GPIO.HIGH)
    GPIO.output(PINK_LED, GPIO.HIGH)


# -----------------------------
# ALERT STATES
# -----------------------------
def blink_blue(duration=15):
    """Clear day → Blue LED blinks, pink stays ON"""
    GPIO.output(PINK_LED, GPIO.HIGH)

    end_time = time.time() + duration
    while time.time() < end_time:
        GPIO.output(BLUE_LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(BLUE_LED, GPIO.LOW)
        time.sleep(0.5)

    idle_weather()


def blink_pink(duration=15):
    """Rain/severe weather → Pink LED blinks, blue stays ON"""
    GPIO.output(BLUE_LED, GPIO.HIGH)

    end_time = time.time() + duration
    while time.time() < end_time:
        GPIO.output(PINK_LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(PINK_LED, GPIO.LOW)
        time.sleep(0.5)

    idle_weather()


# -----------------------------
# CLEANUP (optional)
# -----------------------------
def cleanup():
    GPIO.cleanup()
