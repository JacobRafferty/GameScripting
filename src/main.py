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

        # print(f"Matching confidence: {max_val * 100:.2f}%")

        # If the confidence is above the threshold, click
        if max_val >= confidence_threshold:
            center_x = max_loc[0] + template_width // 2
            center_y = max_loc[1] + template_height // 2
            # print(f"Match found at: ({center_x}, {center_y})")

            pyautogui.click(center_x, center_y)
            # print("Clicked on the matched location.")
        else:
            pass
            # print("No match found with sufficient confidence.")

    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    template_5g = os.getcwd() + "\\5g_claim.png"
    floating_template = os.getcwd() + "\\floating_down.png"
    floating_template = os.getcwd() + "\\floating_left.png"
    floating_template = os.getcwd() + "\\floating_right.png"
    retry_template = os.getcwd() + "\\retry_bigger.png"
    print(template_5g)

    while True:    
        match_template(template_5g)
        match_template(floating_template)
        match_template(floating_template)
        match_template(floating_template)
        match_template(retry_template)
        # time.sleep(2)
