import cv2

def take_snapshot():
    # Initialising cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # Reading thed frames while camera is ON.
        ret, frame = videoCaptureObject.read()
        # cv2.imwrite() method is used to save an image to any storage device.
        cv2.imwrite("NewPicture1.jpg", frame)
        result = False
        
        # Release the camera
        videoCaptureObject.release()
    
         # Closes all the window that might be open while this process
        cv2.destroyAllWindows()

take_snapshot()
