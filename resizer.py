import cv2
name = './img/sensemakers.png'
img = cv2.imread(name)
res = cv2.resize(img,(250, 150), interpolation = cv2.INTER_CUBIC)
cv2.imwrite(name,res)
