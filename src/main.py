import cv2
import numpy as np
import pyautogui
import sys
import os
import time

user = "jacob"
dir = os.getcwd()
template_5g = dir + "\\jacob_img\\5g_claim.png"
floating_template_d = dir + "\\jacob_img\\floating_down.png"
floating_template_l = dir + "\\jacob_img\\floating_left.png"
floating_template_r = dir + "\\jacob_img\\floating_right.png"
retry_template = dir + "\\jacob_img\\retry_bigger.png"
defense_stats_template = dir + "\\jacob_img\\defense_stats.png"
health_template = dir + "\\jacob_img\\health.png"

gem_templates = [
    # os.getcwd() + "\\jacob_img\\\\retry_bigger.png",
    dir + "\\jacob_img\\floating_down.png",
    dir + "\\jacob_img\\floating_left.png",
    dir + "\\jacob_img\\floating_right.png",
    dir + "\\jacob_img\\5g_claim.png"
    # os.getcwd() + "\\jacob_img\\health.png"
]

new_perk_template = f"{dir}\\jacob_img\\perk_imgs\\new_perk.png"
exit_perk_template = f"{dir}\\jacob_img\\perk_imgs\\exit_perks.png"

perk_templates = [
    f"{dir}\\jacob_img\\perk_imgs\\perk_wave_req.png"
    f"{dir}\\jacob_img\\perk_imgs\\gold_tower_bonus.png"
    f"{dir}\\jacob_img\\perk_imgs\\health.png"
    f"{dir}\\jacob_img\\perk_imgs\\free_upgrade_chance.png"
    f"{dir}\\jacob_img\\perk_imgs\\extra_orb.png"
    f"{dir}\\jacob_img\\perk_imgs\\defence_percent.png"
    f"{dir}\\jacob_img\\perk_imgs\\coin_bonus.png"
    f"{dir}\\jacob_img\\perk_imgs\\uw_unlock.png"
    f"{dir}\\jacob_img\\perk_imgs\\game_speed.png"
    f"{dir}\\jacob_img\\perk_imgs\\damage.png"
    f"{dir}\\jacob_img\\perk_imgs\\bounce.png"
    f"{dir}\\jacob_img\\perk_imgs\\cash_bonus.png"
    f"{dir}\\jacob_img\\perk_imgs\\lightning_dmg.png"
    f"{dir}\\jacob_img\\perk_imgs\\spotlight_bonus.png"
    f"{dir}\\jacob_img\\perk_imgs\\smart_missiles.png"
    f"{dir}\\jacob_img\\perk_imgs\\landmine_damage.png"
    f"{dir}\\jacob_img\\perk_imgs\\interest.png"
    f"{dir}\\jacob_img\\perk_imgs\\bossFast_but_weaker.png"
    f"{dir}\\jacob_img\\perk_imgs\\damage_but_bossHealth.png"
    f"{dir}\\jacob_img\\perk_imgs\\enemyDamage_but_lessDmg.png"
    f"{dir}\\jacob_img\\perk_imgs\\lessEnemyHp_but_noRegen.png"
    f"{dir}\\jacob_img\\perk_imgs\\moreLifesteal_but_lessKnockback.png"
    f"{dir}\\jacob_img\\perk_imgs\\shorterRangedAttks_but_strongerAttks.png"
    f"{dir}\\jacob_img\\perk_imgs\\slowEnemy_but_moreDamage.png"
    f"{dir}\\jacob_img\\perk_imgs\\coins_but_maxHpLess.png"
]


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


def click_health():
    success, x, y = match_template(health_template)
    if success:
        click(success, x + 120, y)

def click_gems():
    for template in gem_templates:
        success, x, y = match_template(template)
        if success:
            click(success, x, y)

def click_perk():
    success, x, y = match_template(new_perk_template)
    if success:
        click(success, x, y)

        for template in perk_templates:
            success, x, y = match_template(template)
            if success and (y < 480):
                click(success, x, y)
                print(f"x: {x} y: {y}")
                break
        if not success:
            click (True, 230, 220)
        
        success, x, y = match_template(exit_perk_template)
        click(success, x, y)
        
def click_retry():
    success, x, y = match_template(retry_template)
    click(success, x, y)
    if success:
        once = False
        time.sleep(1)
        while once is False:
            once, x, y = match_template(retry_template)
            click(once, x, y)
    

def main():

    try:
        print('loop')
        health_iter = 0
        daily_mission_iter = 7200

        while True:

            click_gems()
            click_perk()

            if health_iter > 4:
                click_health()
                health_iter = 0
            
            click_retry()

            time.sleep(0.5)

    except Exception as e:
        print(f"Exception: {e}")
        main()

    # iter = 0

    # while True:
    #     iter += 1
    #     retry_clicked = False
    #     success = False

    #     for template_path in gem_templates:
    #         success, x, y = match_template(template_path)
    #         click(success, x, y)

    #     if iter == 20:
    #         success, x, y = match_template(health_template)
    #         click(success, x + 120, y)
    #         iter = 0
        
    #     retry_clicked, x, y = match_template(retry_template)
    #     click(retry_clicked, x, y)

    #     if retry_clicked:
    #         once = False
    #         time.sleep(1)
    #         while once is False:
    #             once, x, y = match_template(defense_stats_template)
    #             click(once, x, y)

    #     time.sleep(0.1)
        # match_template(template_5g)
        # match_template(floating_template_d)
        # match_template(floating_template_l)
        # match_template(floating_template_r)
# just iterate over the prio list and rip the first perk that passes