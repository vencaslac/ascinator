import cv2
import time
import os

cap=cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    img_grayscale=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_grayscale=cv2.resize(img_grayscale,(96,48))

    img_grayscale=img_grayscale/255

    chars=[' ',' ','.','-','=','x','o','#','@']

    #chars=[' ','.',',','-','*']

    img_grayscale=img_grayscale*(len(chars)-1)

    ascii=[]

    for line in img_grayscale:
        lain=[]
        for char in line:
            lain=lain+[chars[int(round(char))]]
        lain=''.join(lain)
        ascii=ascii+[lain]

    ascii='\n'.join(ascii)

    os.system('cls')
    print(ascii)
    key = cv2.waitKey(10)
    if key == 27:
        break

cv2.destroyAllWindows()
cv2.VideoCapture(0).release()
