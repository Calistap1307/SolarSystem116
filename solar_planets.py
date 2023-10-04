import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("Output",img)

cv2.waitKey(0)

cv2.putText(
    img,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Mercury",
    (118,250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255)
)

cv2.putText(
    img,
    "Venus",
    (195,258),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255)
)

cv2.putText(
    img,
    "Earth",
    (290,262),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255)
)

cv2.putText(
    img,
    "Mars",
    (385,258),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255)
)

cv2.putText(
    img,
    "Jupiter",
    (560,380),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255)
)

cv2.putText(
    img,
    "Saturn",
    (775,310),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255)
)

cv2.putText(
    img,
    "Uranus",
    (972,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255)
)

cv2.putText(
    img,
    "Neptune",
    (1120,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,255)
)

cv2.imwrite("Solar_systemwithname.jpg",img)