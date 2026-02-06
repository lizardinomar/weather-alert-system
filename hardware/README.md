# Hardware Setup - Weather Alert System
This documents explains the hardware section of the Weather Alert System. It inclues all LED wiring, GPIO pin use, and hardware testing. 

## Supported Hardware
- Raspberry Pi (tested on Raspberry Pi OS)
- GPIO-controlled LEDs
- Optional breadboard and resistors (220–330Ω recommended)

## Components
- Raspberry Pi (3, 4, or Zero).
- 2 LEDs:
- Blue → Indicates a clear day.
- Pink → Indicates rain or severe weather.
- Resistors (220–330Ω recommended).
- Breadboard and jumper wires.
- Optional buzzer for audio alerts.

## LED Indicators
| LED Color | Meaning                            |
| --------- | ---------------------------------- |
| Blue  | Clear Skies: Sunny or Cloudy   |
| Pink   | Rainy days: Rain or storms   |
| ⚪ Off     | Neutral / no alert / startup state |
Both LEDs are on at all times, but only one blinks. 

## GPIO Pin Mapping
Default GPIO configuration (BCM mode):
| LED | GPIO Pin                            |
| --------- | ---------------------------------- |
| Blue  | GPIO 29  |
| Pink   | GPIO 31   |

Pins can be changed at any time.

## Wiring
- **Blue LED**
  - Anode (long leg) → GPIO Pin 29.
  - Cathode (short leg) → GND via resistor.
- **Pink LED**
  - Anode → GPIO Pin 31.
  - Cathode → GND via resistor.
- Connect all grounds to the Pi’s GND pin.
- Resistors should be placed **in series with the LEDs** to prevent overcurrent.

## Wiring Diagram

![Wiring](hardware/wt_diagram.png)

## Hardware Test
To verify the system is working:
python3 weather_led_test.py

### End of hardware documentation. 
