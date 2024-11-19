import cv2 as cv
from mss import mss
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import screeninfo
import argparse

def click_location(monitor_num, location):
    monitors = screeninfo.get_monitors()
    tower_screen = monitors[monitor_num]
    x_abs = tower_screen.x + location[0]
    y_abs = tower_screen.y + location[1]
    pyautogui.FAILSAFE = False
    pyautogui.click(x_abs, y_abs)
    print(f"Clicked at ({x_abs}, {y_abs}) on Monitor 2.")



def get_screen(monitor):
    with mss() as sct:
        screen = sct.shot(mon=monitor, output='screen.png')
        print(f"sc name: {screen}")
    screen = cv.imread('screen.png', cv.IMREAD_GRAYSCALE)
    return screen




def main():
    parser = argparse.ArgumentParser(description="The Tower Automated")
    parser.add_argument("-m", '--monitor', default=1)

    args = parser.parse_args()

    # get your screen
    screen = get_screen(args.monitor)
    matching_method = getattr(cv, 'TM_CCOEFF')

    # grab template for gems
    gems5_template = cv.imread('C:\\Users\\jacob\\Documents\Projects\\TheTowerAutomation\\img\\5g_closer.png', cv.IMREAD_GRAYSCALE)
    # w, h = gems5_template.shape[::-1]

    # grab template for restart

    # LOOP

    # grab sc
        # see if we can return false on a failed template match

    # match the template
    matched_gems = cv.matchTemplate(screen, gems5_template, matching_method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(matched_gems)

    # click the 5g 
    click_location(args.monitor, max_loc)

    # if you get a restart match, click it
 


if __name__ == "__main__":
    main()



# cv.rectangle(screen,top_left, bottom_right, 255, 2)

# plt.subplot(121),plt.imshow(res,cmap = 'gray')
# plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(screen,cmap = 'gray')
# plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.suptitle(template_method)
# plt.show()

