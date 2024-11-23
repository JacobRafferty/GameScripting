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

            pyautogui.click(center_x, center_y)
            return True
        else:
            return False

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    template_5g = os.getcwd() + "\\jacob_img\\\\5g_claim.png"
    floating_template_d = os.getcwd() + "\\jacob_img\\floating_down.png"
    floating_template_l = os.getcwd() + "\\jacob_img\\floating_left.png"
    floating_template_r = os.getcwd() + "\\jacob_img\\floating_right.png"
    retry_template = os.getcwd() + "\\jacob_img\\retry_bigger.png"
    defense_stats_template = os.getcwd() + "\\jacob_img\\defense_stats.png"
    health_template = os.getcwd() + "\\jacob_img\\health.png"

    templates = [
        # "\\jacob_img\\\\retry_bigger.png",
        "\\jacob_img\\floating_down.png",
        "\\jacob_img\\floating_left.png",
        "\\jacob_img\\floating_right.png",
        "\\jacob_img\\5g_claim.png",
        "\\jacob_img\\health.png"
    ]

    while True:    
        for template_path in templates:
            match_template(template_path)
        
        retry_clicked = match_template(retry_template)

        if retry_clicked:
            once = False
            time.sleep(1)
            while once is False
                once = match_template(defense_stats_template)

        time.sleep(0.1)
        # match_template(template_5g)
        # match_template(floating_template_d)
        # match_template(floating_template_l)
        # match_template(floating_template_r)
