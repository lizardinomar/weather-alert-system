import RPi.GPIO as GPIO
import time

# GPIO pin setup
BLUE_LED = 5   # Physical Pin 29
PINK_LED = 6   # Physical Pin 31

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(PINK_LED, GPIO.OUT)

print("Starting Weather LED test. Press CTRL+C to stop.")

try:
    while True:
        # Turn Blue LED on, Pink LED off
        GPIO.output(BLUE_LED, True)
        GPIO.output(PINK_LED, False)
        time.sleep(0.5)

        # Turn Pink LED on, Blue LED off
        GPIO.output(BLUE_LED, False)
        GPIO.output(PINK_LED, True)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping Weather LED test...")
finally:
    GPIO.output(BLUE_LED, False)
    GPIO.output(PINK_LED, False)
    GPIO.cleanup()
