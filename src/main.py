import cv2
import numpy as np
import pyautogui
import sys
import os
import time

def match_template(template_path, confidence_threshold=0.7):
    try:
        template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
        if template is None:
            print(f"Error: Could not load template image from {template_path}")
            return

        if len(template.shape) == 3:  # Check if the image is not already grayscale
            template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        template_height, template_width = template.shape[:2]

        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence_threshold:
            center_x = max_loc[0] + template_width // 2
            center_y = max_loc[1] + template_height // 2
            return True, center_x, center_y
        else:
            return False, 0, 0

    except Exception as e:
        print(f"Error: {e}")

def click(valid, x, y):
    if valid:
        pyautogui.click(x, y)
    else:
        pass


if __name__ == "__main__":
    template_5g = os.getcwd() + "\\jacob_img\\5g_claim.png"
    floating_template_d = os.getcwd() + "\\jacob_img\\floating_down.png"
    floating_template_l = os.getcwd() + "\\jacob_img\\floating_left.png"
    floating_template_r = os.getcwd() + "\\jacob_img\\floating_right.png"
    retry_template = os.getcwd() + "\\jacob_img\\retry_bigger.png"
    defense_stats_template = os.getcwd() + "\\jacob_img\\defense_stats.png"
    health_template = os.getcwd() + "\\jacob_img\\health.png"

    templates = [
        # os.getcwd() + "\\jacob_img\\\\retry_bigger.png",
        os.getcwd() + "\\jacob_img\\floating_down.png",
        os.getcwd() + "\\jacob_img\\floating_left.png",
        os.getcwd() + "\\jacob_img\\floating_right.png",
        os.getcwd() + "\\jacob_img\\5g_claim.png"
        # os.getcwd() + "\\jacob_img\\health.png"
    ]
    iter = 0

    while True:
        iter += 1
        retry_clicked = False
        success = False

        for template_path in templates:
            success, x, y = match_template(template_path)
            click(success, x, y)

        if iter == 20:
            success, x, y = match_template(health_template)
            click(success, x + 120, y)
            iter = 0
        
        retry_clicked, x, y = match_template(retry_template)
        click(retry_clicked, x, y)

        if retry_clicked:
            once = False
            time.sleep(1)
            while once is False:
                once, x, y = match_template(defense_stats_template)
                click(once, x, y)

        time.sleep(0.1)
        # match_template(template_5g)
        # match_template(floating_template_d)
        # match_template(floating_template_l)
        # match_template(floating_template_r)
