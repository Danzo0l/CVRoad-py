import cv2 as cv
import numpy as np
import road_detection as rd
import logs

logs.clean_log()

video = cv.VideoCapture('videoplayback.mp4')

if not video.isOpened():
    logs.is_error('file is not opened')
else:
    logs.is_complied('file opened')

cv.waitKey(1)

while video.isOpened():
    _, frame = video.read()
    cv.resizeWindow("Detecting_road", 1300, 800)

    copy_img = np.copy(frame)
    frame = rd.region_of_interest(frame)
    #frame = rd.canny(frame)
    cv.imshow("Detecting_road", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv.destroyAllWindows()