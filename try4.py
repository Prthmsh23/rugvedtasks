import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt

# Define the color boundaries of the ball in the HSV color space
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

# Initialize the list for storing past positions
pts = []

# Open the video file
vs = cv2.VideoCapture('VID-20231117-WA0090.mp4')

# Initialize lists for storing x and y coordinates
x_coords = []
y_coords = []

while True:
 # Grab the current frame
 ret, frame = vs.read()

 # If we did not grab a frame, then we have reached the end of the video
 if not ret:
    break

 # Resize the frame, blur it, and convert it to the HSV color space
 frame = imutils.resize(frame, width=600)
 blurred = cv2.GaussianBlur(frame, (11, 11), 0)
 hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

 # Construct a mask for the color "green", then perform a series of dilations and erosions to remove any small blobs left in the mask
 mask = cv2.inRange(hsv, greenLower, greenUpper)
 mask = cv2.erode(mask, None, iterations=2)
 mask = cv2.dilate(mask, None, iterations=2)

 # Find contours in the mask and initialize the current (x, y) center of the ball
 cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 cnts = imutils.grab_contours(cnts)
 center = None

 # Only proceed if at least one contour was found
 if len(cnts) > 0:
    # Find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
    c = max(cnts, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    # Only proceed if the radius meets a minimum size
    if radius > 10:
        # Draw the circle and centroid on the frame, then update the list of tracked points
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)

 # Append the center to the list of tracked points
 pts.append(center)

 # Remove the oldest point if the list has reached its maximum size
 if len(pts) > 64:
    pts.pop(0)

 # Store the x and y coordinates of the center in separate lists
 if center is not None:
    x_coords.append(center[0])
    y_coords.append(center[1])

 # Show the frame to our screen
 cv2.imshow("Frame", frame)
 key = cv2.waitKey(1) & 0xFF

 # If the 'q' key is pressed, stop the loop
 if key == ord("q"):
    break

# Release the video capture and destroy windows
vs.release()
cv2.destroyAllWindows()

# Plot the x and y coordinates
plt.figure(figsize=(10, 5))
plt.plot(x_coords, y_coords, 'ro-')
plt.title('Ball Tracking')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
