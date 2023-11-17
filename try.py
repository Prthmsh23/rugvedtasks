
import cv2

cap = cv2.VideoCapture('VID-20231117-WA0090.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    #to convert frame into greyscale, then blur it then perform canny edge function
    edges = cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), (11,11), 0), 100, 170)
    
    #to display the frame
    cv2.imshow('edges after hough lines', edges)
    
    #escape key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cap.destroyAllWindows()