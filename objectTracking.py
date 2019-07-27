import numpy as np
import argparse
import time
import cv2
from imutils.video import VideoStream
import datetime
import imutils
import math

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (Optional) video file")
args = vars(ap.parse_args())

# Greater than lower, lesser than higher
# BGR (Order)
grapeLower = np.array([27, 6, 4], dtype="uint8")
grapeHigher = np.array([123, 93, 91], dtype="uint8")

if args.get("video", None) is None:
    camera = VideoStream(src=0).start()
    time.sleep(2.0)

# otherwise, we are reading from a video file
else:
    camera = cv2.VideoCapture(args["video"])

firstFrame = None

while True:
    # read() method returns a tuple of two values
    # Grabbed => Boolean of if frame is successfully read
    # Frame => frame itself
    frame = camera.read()

    frame = frame if args.get("video", None) is None else frame[1]

    if frame is None:
        break
    # Pixel within range is white, otherwise black
    grape = cv2.inRange(frame, grapeLower, grapeHigher)

    # find the colors within the specified boundaries and apply the mask
    # set in bound to white


    # Show only pixels that have white

    grape = cv2.GaussianBlur(grape, (3, 3), 0)

    # Use copy() because findContours() is destructive
    (cnts, _) = cv2.findContours(grape.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)
        # minAreaRect computes min bonding box;
        # boxPoints re-shape the box to a list of points
        for i in range(len(cnts)):
            area = cv2.contourArea(cnt[i])
            perimeter = cv2.arcLength(cnt[i], True)

            if (math.sqrt(area) > (perimeter / 4.5)) and (area > 100):
                rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt[i])))
                cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", grape)

    time.sleep(0.025)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
