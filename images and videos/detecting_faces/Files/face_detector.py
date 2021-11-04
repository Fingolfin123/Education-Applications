#Use openCV to compare image to haarcascade
import cv2


def detectFaces(cascade,image,scaleFactor,neighbors):
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + cascade)

    #print(face_cascade.empty())
    img=cv2.imread(image)
    #cv2.imshow("Photo",img)
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("GrayPhoto",gray_img)
    faces=face_cascade.detectMultiScale(gray_img,
    scaleFactor=scaleFactor,
    minNeighbors=neighbors)

    for x, y, w, h in faces:
        img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

    print(type(faces))
    print(faces)

    resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

    cv2.imshow("Gray",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detectFaces('haarcascade_frontalface_default.xml',"news.jpg",1.1,5)
