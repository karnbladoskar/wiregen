import cv2
import time
import numpy as np

class GetRecording:
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    defl
video_out = "recordedVid.avi"

# Define the codec and creade VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
video_writer = cv2.VideoWriter(video_out, fourcc, 20.0, (self.WIDTH, self.HEIGHT))

cap = cv2.VideoCapture(0)
t = time.time()
t3 = 0
while( t3 < 10):   #(cap.isOpened()) for continuous recording
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        video_writer.write(np.uint8(frame))

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    t2 = time.time()
    t3 = t2 - t
    print("Time passed: %d", t3)

cap.release()
video_writer.release()
cv2.destroyAllWindows() 

