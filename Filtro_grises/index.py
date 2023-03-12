import cv2
imagenvideo = cv2.VideoCapture(0);

if not imagenvideo.isOpened():
    print("No se reconoce la camara");
    exit()

while True:
    tipocamara,camara=imagenvideo.read()
    grises=cv2.cvtColor(camara,cv2.COLOR_BGR2GRAY)
    cv2.imshow("En vivo", grises)

    if cv2.waitKey(1)==ord("q"):
        break

imagenvideo.release()
cv2.destroyAllWindows
