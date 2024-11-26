import cv2
import numpy as np
import pyautogui
import os
import time

user = "wyatt"
dir = os.getcwd()
        
gemTemplates = [
f"{dir}\\src\\{user}_img\\5g_test.png",
f"{dir}\\src\\{user}_img\\gem_down.png",
f"{dir}\\src\\{user}_img\\gem_left.png",
f"{dir}\\src\\{user}_img\\gem_right.png"
]
        
newPerkTemplate = f"{dir}\\src\\{user}_perks\\new_perk.png"
exitPerkTemplate = f"{dir}\\src\\{user}_perks\\exit_perk.png"
perkTemplates = [
    f"{dir}\\src\\{user}_perks\\wave_req_perk.png",
    f"{dir}\\src\\{user}_perks\\gt_perk.png",
    f"{dir}\\src\\{user}_perks\\extra_dw_perk.png",
    f"{dir}\\src\\{user}_perks\\max_hp_perk.png",
    f"{dir}\\src\\{user}_perks\\free_upgrade_perk.png",
    f"{dir}\\src\\{user}_perks\\extra_orb_perk.png",
    f"{dir}\\src\\{user}_perks\\percent_def_perk.png",
    f"{dir}\\src\\{user}_perks\\coin_perk.png",
    f"{dir}\\src\\{user}_perks\\ultimate_weapon_perk.png",
    f"{dir}\\src\\{user}_perks\\bh_perk.png",
    f"{dir}\\src\\{user}_perks\\game_speed_perk.png",
    f"{dir}\\src\\{user}_perks\\bounce_shot_perk.png",
    f"{dir}\\src\\{user}_perks\\damage_perk.png",
    f"{dir}\\src\\{user}_perks\\cash_perk.png",
    f"{dir}\\src\\{user}_perks\\chain_dmg_perk.png",
    f"{dir}\\src\\{user}_perks\\landmine_dmg_perk.png",
    f"{dir}\\src\\{user}_perks\\dmg_reduction_perk.png",
    f"{dir}\\src\\{user}_perks\\dmg_health_perk.png",
    f"{dir}\\src\\{user}_perks\\extra_ilm_perk.png",
    f"{dir}\\src\\{user}_perks\\boss_health_boss_speed_perk.png",
    f"{dir}\\src\\{user}_perks\\enemy_health_reduction_lifesteal_reduction_perk.png",
    f"{dir}\\src\\{user}_perks\\four_smart_missile_perk.png",
    f"{dir}\\src\\{user}_perks\\def_abs_perk.png",
    f"{dir}\\src\\{user}_perks\\health_regen_perk.png",
    f"{dir}\\src\\{user}_perks\\enemy_range_reduction_perk.png",
    f"{dir}\\src\\{user}_perks\\less_boss_health_perk.png",
    f"{dir}\\src\\{user}_perks\\interest_perk.png",
    f"{dir}\\src\\{user}_perks\\enemy_slow_perk.png",
    f"{dir}\\src\\{user}_perks\\no_knockback_perk.png",
    f"{dir}\\src\\{user}_perks\\useless_perk.png"
]
        
health_template = f"{dir}\\src\\{user}_img\\health_small.png"
retry_template = f"{dir}\\src\\{user}_img\\retry_bigger.png"
health_workshop_template = f"{dir}\\src\\{user}_img\\health_shop_big.png"

active_run_menu_template = f"{dir}\\src\\{user}_img\\active_run_menu.png"
active_daily_task_notification_template = f"{dir}\\src\\{user}_img\\active_daily_task_notification.png"
claim_daily_task_template = f"{dir}\\src\\{user}_img\\claim_daily_task.png"
chest_available_template = f"{dir}\\src\\{user}_img\\chest_available.png"
next_template = f"{dir}\\src\\{user}_img\\next.png"
claim_template = f"{dir}\\src\\{user}_img\\claim.png"
tap_to_return_to_game_template = f"{dir}\\src\\{user}_img\\tap_to_return_to_game.png"

def main():
    try:
        print("Running loop...")
        healthCounter = 0
        dailyMissionCounter = 3598
        
        while True:
            if (healthCounter > 4):
                click_health()
                healthCounter = 0
            else:
                healthCounter = healthCounter + 1
                
            click_gems()
            click_perk()
            #Every ~2 hours 
            if (dailyMissionCounter > 3600):
                check_daily_missions()
                dailyMissionCounter = 0
            else:
                dailyMissionCounter = dailyMissionCounter + 1
                
            click_retry()
            time.sleep(1)
    except Exception as error:
        print("Error:" + str(error))
        main()

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
            if 'health_small' in template_path:
                center_x = max_loc[0] + template_width // 2
                center_y = max_loc[1] + template_height // 2
                # print(f"Match found at: ({center_x}, {center_y})")
                
                clickPoint_x = center_x + 150
                return(True, clickPoint_x, center_y)
                
                #pyautogui.click(clickPoint_x , center_y)
                # print("Clicked on the matched location.")
            else:
                center_x = max_loc[0] + template_width // 2
                center_y = max_loc[1] + template_height // 2
                # print(f"Match found at: ({center_x}, {center_y})")

                return(True, center_x, center_y)
                #pyautogui.click(center_x, center_y)
                # print("Clicked on the matched location.")
        else:
            return (False, 0, 0)
            # print("No match found with sufficient confidence.")

    except Exception as e:
        print(f"Error: {e}")

def click(send_it, x, y):
    if send_it:
        pyautogui.click(x , y)
        
        
def click_gems():
    #Search for gems    
    for template in gemTemplates:
        success, x, y = match_template(template)
        click(success, x, y)    
    return 

def click_health():
    #Search for health upgrade
    success, x, y = match_template(health_template)
    if (success):
        #If the health upgrade is found, click it.
        click(success, x, y)
    else:
        #Otherwise search and click on the health workshop, then click the health upgrade.
        success, x, y = match_template(health_workshop_template)
        click(success, x, y)
        time.sleep(0.5)
        success, x, y = match_template(health_template)
        click(success, x, y)
    return

def click_retry():
    #Search for retry
    success, x, y = match_template(retry_template)
    click(success, x, y)
    return

def click_perk():
    #Search for New Perk Banner
    success, x, y = match_template(newPerkTemplate)
    if success:
        #Click on the new perk banner
        click(success, x, y)
        #Iterate through ranked perk list until we find an available perk.
        for template in perkTemplates:
            success, x, y = match_template(template)
            if success and (y<480):
                click(success, x, y)
                print(f"x:{x}, y:{y}")
                break #Once we click a perk we can stop running through our list.
        if not success:
            #If we don't find a perk, click the top one. 
            click(True, 950, 295)
        #click the exit button
        success, x, y = match_template(exitPerkTemplate)
        click(success, x, y)
    return

def check_daily_missions():
    success, x, y = match_template(active_run_menu_template)
    click(success, x, y)
    time.sleep(0.5)
    
    success, x, y = match_template(active_daily_task_notification_template)
    click(success, x, y)
    time.sleep(0.5)
    
    success, x, y = match_template(claim_daily_task_template)
    while(success):
        click(success, x, y)
        success, x, y = match_template(claim_daily_task_template)
        time.sleep(0.5)
    
    success, x, y = match_template(chest_available_template)
    if success:
        click(success, x, y)
        success, x, y = match_template(next_template)
        click(success, x, y)
        success, x, y = match_template(claim_template)
        click(success, x, y)
        time.sleep(0.5)
     
    success, x, y = match_template(tap_to_return_to_game_template) 
    click(success, x, y)
    time.sleep(0.5)
    
    return

if __name__ == "__main__":
    main()
