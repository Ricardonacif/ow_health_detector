import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob, os

def apply_threshold(imgpath, index):
  img = cv2.imread(imgpath, 0)
  blur = cv2.GaussianBlur(img,(5,5),0)
  ret3,threshold = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


  
  count, labels, stats, centroids = cv2.connectedComponentsWithStats(threshold)
  print(stats)
  # cv2.imshow('threshold' + str(index), threshold)
  for x, y, w, h, a in stats[1:]:
    # if a > 90:
      region = threshold[y:y+h, x:x+w]
      plt.imshow(region, interpolation='none')
      # cv2.imwrite('result'+ str(x), region)
      plt.show()



  # cv2.imshow('threshold2' + str(index), im2)


def compare_images(img, img2):
  res = cv2.matchTemplate(img, img2,cv2.TM_CCOEFF_NORMED)
  return res



# for index, pathAndFilename in enumerate(glob.iglob(os.path.join('test_images', '*.png'))):
#   print(str(index))
#   apply_threshold(pathAndFilename, index)

apply_threshold('test_images/23.png', 1)

cv2.waitKey(0)
cv2.destroyAllWindows()









# def rename(dir, pattern):
#     i = 0
#     for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
#         title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#         os.rename(pathAndFilename, os.path.join(dir, str(i) + '.png'))
#         i = i+1



# rename(r'test_images', r'*.png')