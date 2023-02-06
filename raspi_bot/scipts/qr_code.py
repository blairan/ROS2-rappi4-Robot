import cv2

img=cv2.imread("raspi_bot/scipts/stop.png")

detector = cv2.QRCodeDetector()

data, point, rect = detector.detectAndDecode(img)

print(data)


cv2.imshow("Dectotion qr", img)
cv2.waitKey(0)
cv2.destroyAllWindows()