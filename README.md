# Leap Desktop Controller For Linux

This python script allow you to control your desktop (Gnome) of your linux machine.

You Can Find More Details and How it Works on my [Youtube](https://www.youtube.com) Channel.

## Motions :

* UP : Maximize Current Window
* Down : Minimize Current Window
* Right : Resize Current Window to Half Right of Display
* Left : Resize Current Window to Half Left of Display
* Tap : Simulate Enter(Return) Button
* Finger Clockwise Rotate : Increase Sound Volume
* Finger Counterclockwise Rotate : Decrease Sound Volume

## Dependencies

* Leap SDK
  * download and install from https://developer.leapmotion.com/sdk/v2
* Leap driver
  * download and install from https://leapmotion.com/setup
* xdotool
  ```
  sudo apt install xdotool -y
  ```
* python
  ```
  sudo apt install python -y
  ```

## Executing

```
    python desktopController.py
```
## Troubleshooting

1 - Double check all Dependencies are installed.

2 - This script needs these file from Leap SDK, if current files are not working with your linux copy theme from your Leap SDK folder :
```
Leap.py
Leap.pyc
LeapPython.so
libLeap.so
```
3 - Check leapd daemon is running . if not, run this command in another terminal from root user:
```
leapd
```

4 - if problem still presents tell me in issues tap , i will help you :)

## License

GPLv3
