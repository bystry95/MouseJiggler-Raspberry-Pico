# Raspberry Pi Pico CapsLock Jiggler

🕺💡 This project is inspired by [TomasHubelbauer's Raspi Mouse Jiggler](https://github.com/TomasHubelbauer/raspi-mouse-jiggler) and has been reworked to create a Raspberry Pi Pico CapsLock Jiggler. Instead of moving the mouse cursor, this project automatically presses the CapsLock key every 60 seconds, simulating user activity to prevent system lockouts or sleep modes.

## Introduction

👋 Hello Easywalker! Welcome to the Raspberry Pi Pico CapsLock Jiggler project.

## Requirements

To use this project, you will need the following:

- Raspberry Pi Pico microcontroller
- Micro USB cable (for power and data connection)
- [Adafruit CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) (version 8.2.0 or higher)
- `adafruit_hid` library (included in the repository)
- Code file (`code.py`)

## Installation

Follow these steps to set up the Raspberry Pi Pico CapsLock Jiggler:

1. Connect the Raspberry Pi Pico to your computer using the micro USB cable. Make sure to hold the button while connecting to enter the bootloader mode.

2. Copy the `adafruit-circuitpython-raspberry_pi_pico-en_GB-8.2.0.uf2` file to the Pico device. Wait for the device to reboot and remount.

3. Copy the `adafruit_hid` folder to the `lib` folder on the Pico. This folder contains the necessary HID (Human Interface Device) library for emulating key presses.

4. Copy the `code.py` file to the root directory of the Pico.

5. Finito! Your Raspberry Pi Pico CapsLock Jiggler is now ready to use.

## Usage

Once you have completed the installation steps, the Raspberry Pi Pico will automatically simulate the pressing of the CapsLock key every 60 seconds. This activity will prevent your system from going into sleep mode or locking the screen due to inactivity.

Make sure to keep the Pico connected to your computer or a power source for continuous operation.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and adapt it to suit your needs.

## Acknowledgments

- [TomasHubelbauer](https://github.com/TomasHubelbauer) for the original inspiration from the Raspi Mouse Jiggler project.

## Disclaimer

⚠️ Using this project to prevent system lockouts or sleep modes might not comply with the policies or guidelines of your organization or software applications. Make sure to use this project responsibly and adhere to any applicable rules or regulations.

*Note: The Raspberry Pi logo used in the banner image is a trademark of the Raspberry Pi Foundation and is used here for illustrative purposes only.*
