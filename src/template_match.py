import cv2 as cv
from mss import mss
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import screeninfo

# template = "img\\5gem.png"
template = cv.imread('C:\\Users\\jacob\\Documents\Projects\\TheTowerAutomation\\img\\5g_closer.png', cv.IMREAD_GRAYSCALE)
# template2 = template.copy()

# width and height of the template to be matched
w, h = template.shape[::-1]

# take a sc of the screen ( try to replace this with an app capture)
with mss() as sct:
    screen = sct.shot(mon=2, output='screen.png')
    print(f"sc name: {screen}")

screen = cv.imread('screen.png', cv.IMREAD_GRAYSCALE)

template_method = 'TM_CCOEFF'

method = getattr(cv, template_method)

res = cv.matchTemplate(screen, template, method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
print(f'top left: {top_left}')

bottom_right = (top_left[0] + w, top_left[1] + h)

print(f"bottom right: {bottom_right}")



cv.rectangle(screen,top_left, bottom_right, 255, 2)

plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(screen,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(template_method)

# plt.show()


monitors = screeninfo.get_monitors()

tower_screen = monitors[1]

x_abs = tower_screen.x + top_left[0]
y_abs = tower_screen.y + top_left[1]

pyautogui.click(x_abs, y_abs)

print(f"Clicked at ({x_abs}, {y_abs}) on Monitor 2.")
