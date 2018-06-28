#!/usr/bin/env python

import Leap, sys, thread, time, os
from subprocess import call
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):

        # Get the most recent frame and report some basic information
        frame = controller.frame()

        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get gestures
        for gesture in frame.gestures():

            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                    print clockwiseness
                    os.system('xdotool key XF86AudioRaiseVolume')
                    time.sleep(0.3)
                    break
                else:
                    clockwiseness = "counterclockwise"
                    print clockwiseness
                    os.system('xdotool key XF86AudioLowerVolume')
                    time.sleep(0.3)
                    break

                # Calculate the angle swept since the last frame
                """swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START:
                    previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                    swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

                print "  Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (gesture.id, self.state_names[gesture.state],circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness)"""

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                #print "  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (gesture.id, self.state_names[gesture.state],swipe.position, swipe.direction, swipe.speed)
                if abs(swipe.direction.x) > abs(swipe.direction.y) and abs(swipe.direction.x) > abs(swipe.direction.z):
                    isMotionDetected = True
                    if swipe.direction.x > 0:
                        print 'right'
                        os.system('xdotool key super+Right')
                        time.sleep(1)
                        break
                    else :
                        print 'left'
                        os.system('xdotool key super+Left')
                        time.sleep(1)
                        break

                if abs(swipe.direction.y) > abs(swipe.direction.x) and abs(swipe.direction.y) > abs(swipe.direction.z):
                    if swipe.direction.y > 0:
                        print 'up'
                        os.system('xdotool key super+Up')
                        time.sleep(2)
                        break
                    else :
                        print 'down'
                        os.system("xdotool windowminimize $(xdotool getactivewindow)")
                        time.sleep(2)
                        break


            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                isMotionDetected = True
                keytap = KeyTapGesture(gesture)
                #print "  Key Tap id: %d, %s, position: %s, direction: %s" % (gesture.id, self.state_names[gesture.state],keytap.position, keytap.direction )
                print 'tap'
                os.system("xdotool key Return")
                time.sleep(1)
                break


            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                isMotionDetected = True
                screentap = ScreenTapGesture(gesture)
                #print "  Screen Tap id: %d, %s, position: %s, direction: %s" % (gesture.id, self.state_names[gesture.state],screentap.position, screentap.direction )
                print 'tap'
                os.system("xdotool key Return")
                time.sleep(1)
                break

        #if not (frame.hands.is_empty and frame.gestures().is_empty):
            #print ""

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
