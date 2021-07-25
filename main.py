import cv2 as cv
import numpy as np
import road_detection as rd
import logs

logs.clean_log()

video = cv.VideoCapture('videoplayback.mp4')
#cv.resizeWindow('1231', 600, 600)

if not video.isOpened():
    logs.is_error('file is not opened')
else:
    logs.is_complied('file opened')


cv.waitKey(1)

while video.isOpened():
    _, frame = video.read()
    copy_img = np.copy(frame)
    try:
        frame = rd.canny(frame)
        frame = rd.region_of_interest(frame)
        lines = cv.HoughLinesP(frame, 2, np.pi/180, 100, np.array([()]),  minLineLength=20, maxLineGap=5)
        av_lines = rd.average_slope_intercept(frame, lines)
        line_img = rd.display_lines(copy_img, av_lines)
    except:
        pass
        combo = cv.addWeighted(copy_img, 0.8, line_img, 0.5, 1)
        cv.imshow("Detecting_road", combo)


    if cv.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv.destroyAllWindows()
