import numpy as np
import pyautogui
from matplotlib import pyplot as plt

import imutils
import cv2
import pyscreenshot as ImageGrab
import time
import sys
import glob
from blinkstick import blinkstick




def light_red():
    bstick = blinkstick.find_first()
    for bstick in blinkstick.find_all():
        for x in xrange(1,60):
            bstick.set_color(channel=0, index=x, name="red")

def light_green():
    bstick = blinkstick.find_first()
    for bstick in blinkstick.find_all():
        for x in xrange(1,60):
            bstick.set_color(channel=0, index=x, name="green")


def get_health_numbers(imgpath):
  img = cv2.imread(imgpath, 0)
  imgcolor = cv2.imread(imgpath, 1)
  debug_image = imgcolor.copy()
  
  blur = cv2.GaussianBlur(img,(5,5),0)
  ret3,threshold = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  
  # threshold = cv2.erode(threshold, np.ones((2,2)))
  # cv2.imshow("T",threshold)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()

  
  count, labels, stats, centroids = cv2.connectedComponentsWithStats(threshold)
  # print("x, y, w, h, a")
  # print(stats)

  templates = []
  for p in sorted(glob.glob('./number_templates/*.png')):
      templates.append(cv2.imread(p, 0))

  healthDigits = []
  totalHealthDigits = []
  for i, (x, y, w, h, a) in sorted(list(enumerate(stats)), key=lambda e: e[1][0]):
    if i == 0:
        continue
    s = None
    isHealthTotal=False
    if a > 200 and w > 5 and h > 38:
        s = 0.3
    elif a > 55 and w >= 1 and h >= 19:
        isHealthTotal=True
        s = 0.15
    else:
        cv2.rectangle(debug_image, (x,y), (x+w, y+h), (0, 0, 255))
        
    if s:
        region = ((labels == i)[y:y+h, x:x+w] * 255).astype(np.uint8)
        region = cv2.copyMakeBorder(region, 10, 10, 10, 30, cv2.BORDER_CONSTANT, 0)
        digit_match = []
        for i, t in enumerate(templates):
            # cv2.imshow("T",t)
            
            t = cv2.resize(t, (0, 0), fx=s, fy=s)
            # cv2.imshow("T2",t)
            # cv2.imshow("region",region)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            digit_match.append(np.min(cv2.matchTemplate(region, t, cv2.TM_SQDIFF_NORMED)))
            
        digit = np.argmin(digit_match)
        
        cv2.putText(debug_image, '%d' % (digit), (x, y-22), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0))
        cv2.putText(debug_image, '%1.2f' % (digit_match[digit]), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0))
        cv2.rectangle(debug_image, (x,y), (x+w, y+h), (0, 255, 0))
        
        if digit_match[digit] < 0.4:
          if isHealthTotal:
            totalHealthDigits.append(digit)
          else:
            healthDigits.append(digit)
        # else:
        #     # raise ValueError('Could not classify digit %d' % (i, ))

  # cv2.imshow("debug",debug_image)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
  # print(healthDigits)
  # print(totalHealthDigits)
  if healthDigits and totalHealthDigits:
    print("----")
    print(imgpath)
    currentHealth = (''.join(str(d) for d in healthDigits))
    currentMaxHealth = (''.join(str(d) for d in totalHealthDigits))
    print("health:" + currentHealth)
    print("total health:" + currentMaxHealth)
    if int(currentHealth) < 200:
        light_red()
    else:
        # light_green()
        print('')
  else:
    print("coulnt read")





if __name__ == "__main__":
  
    try:
        # get_health_numbers('output/251.png')
        i = 226
        light_green()
        while True:
            # time.sleep(0.1)
            im=ImageGrab.grab(bbox=(350,1205,475,1260)) # X1,Y1,X2,Y2
            # print(pyautogui.size()) 
            
            # im.show()
            im.save("output/" + str(i) + '.png', 'PNG')
            get_health_numbers("output/" + str(i) + '.png')
            # print(i)
            i=i+1
    except KeyboardInterrupt:
        sys.exit()


#-#
