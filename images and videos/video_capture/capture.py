import cv2, time

video=cv2.VideoCapture(0)   #capture video
a=1

while True:
    a=a+1
    check, frame = video.read()

    print(check)#check if video captured
    print(frame)#numpy array, returns first frame

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)   #hold script for 3 seconds
    cv2.imshow("Capturing",gray)
    key = cv2.waitKey(1)#change update rate

    if key==ord('q'):
        break


print(a)

video.release()
cv2.destroyAllWindows
