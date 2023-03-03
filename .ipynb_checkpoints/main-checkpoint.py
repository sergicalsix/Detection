import cv2

def detection_mask(img_path):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

    
    img = cv2.imread(img_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    mask_flag = True
    if len(faces) > 0:
        (x,y,w,h) = faces[0] #最初の一人

        roi_gray = gray[y:y+h, x:x+w]

        roi_color = img[y:y+h, x:x+w]

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        tmp_mouth = mouth_cascade.detectMultiScale(roi_gray)

        if len(tmp_mouth) > 0:
            #tmp_mouth_len = len(tmp_mouth)
            (mx,my,mw,mh) =  tmp_mouth[-1] #口候補のうち最後のもの

            cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,255,255),2)
            mask_flag = False

    if mask_flag:
        print('mask!!')
    else:
        print('no mask!!')
    
    cv2.imshow("Image", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

img_path = 'mask.png'
detection_mask(img_path)
