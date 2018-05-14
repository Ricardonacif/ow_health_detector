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

  debug_image = img.copy()

  templates = []
  for p in sorted(glob.glob('./number_templates/*.png')):
      templates.append(cv2.imread(p, 0))

  digits = []
  for i, (x, y, w, h, a) in sorted(list(enumerate(stats)), key=lambda e: e[1][0]):
    if i == 0:
        continue
    s = None
    if a > 500 and w > 10 and h > 50:
        s = 0.4
    elif a > 100 and w > 3 and h > 25:
        s = 0.20
    else:
        cv2.rectangle(debug_image, (x,y), (x+w, y+h), (0, 0, 255))
        
    if s:
        region = ((labels == i)[y:y+h, x:x+w] * 255).astype(np.uint8)
        region = cv2.copyMakeBorder(region, 10, 10, 10, 30, cv2.BORDER_CONSTANT, 0)
        digit_match = []
        for i, t in enumerate(templates):
            t = cv2.resize(t, (0, 0), fx=s, fy=s)
            digit_match.append(np.min(cv2.matchTemplate(region, t, cv2.TM_SQDIFF_NORMED)))
            
        digit = np.argmin(digit_match)
        
        cv2.putText(debug_image, '%d' % (digit), (x, y-22), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0))
        cv2.putText(debug_image, '%1.2f' % (digit_match[digit]), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0))
        cv2.rectangle(debug_image, (x,y), (x+w, y+h), (0, 255, 0))
        
        if digit_match[digit] < 0.4:
            digits.append(digit)
        else:
            raise ValueError('Could not classify digit %d' % (i, ))

  # cv2.imshow("debug",debug_image)
  print(''.join(str(d) for d in digits))




  # cv2.imshow('threshold2' + str(index), im2)


# def compare_images(img, img2):
#   res = cv2.matchTemplate(img, img2,cv2.TM_CCOEFF_NORMED)
#   return res



# for index, pathAndFilename in enumerate(glob.iglob(os.path.join('test_images', '*.png'))):
#   print(str(index))
#   apply_threshold(pathAndFilename, index)

apply_threshold('test_images/23.png', 1)
# img1 = cv2.imread('got0.png', 0)
# img2 = cv2.imread('number_templates/0.png', 0)
# opa = compare_images(img1, img2)

# print(opa)
# cv2.waitKey(0)
# cv2.destroyAllWindows()









# def rename(dir, pattern):
#     i = 0
#     for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
#         title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#         os.rename(pathAndFilename, os.path.join(dir, str(i) + '.png'))
#         i = i+1



# rename(r'test_images', r'*.png')