import math



#alr heres the plan buddy
#make a button to toggle script use. making it stop looking for the winrate
#make settings to change the charachter and background
#make a info thing

#first we limbus, then we company 



#release

import mss #for screen capture
import numpy as np #for array manipulation
import time #for sleep
import cv2 #for image processing
import pydirectinput #for simulating key presses

import threading
import random

#lets make ui, a script is boring and dull
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import PIL.Image, PIL.ImageTk


#for my toggle script
Script_Running = True



#in battle stuff
winrate = cv2.imread("limbus_assets/battle(winrate)/i love winrate.png",0) #load the winrate image
Victory = cv2.imread("limbus_assets/battle(winrate)/victory scene.png",0)

w1, h1 = winrate.shape[::-1]
w2,h2 = Victory.shape[::-1]

battling = True
winrate_just_found = False
victory_just_found = False

#enter room stuff
exploring = False
entered_room_just_found = False

enter_room = cv2.imread("limbus_assets/floors/enter room.png",0) #load the fight image
to_battle = cv2.imread("limbus_assets/battle(winrate)/start battle.png",0)
w3, h3 = enter_room.shape[::-1]
w4, h4 = to_battle.shape[::-1]


threshold = 0.7 #set the threshold for image matching


#window stuff

glow_colors = glow_colors = [
"#aaffcc",
"#66ff99",
"#33ff77",
"#66ff99"
]
glow_index = 0



root = ttk.Window(themename="cosmo")
root.configure(bg="black")
root.title("Limbus Winrate +")
root.geometry("680x480")
root.resizable(False, False)
root.attributes("-topmost", True)



background_list = ["backgrounds/S824.png","backgrounds/Story_Somewhere_in_Hongyuan_BG.png",
"backgrounds/Story_Bridge_to_Tiekan_Temple_BG.png","backgrounds/Story_Hongyuan's_Laboratory,_Past_7_BG.png","backgrounds/Story_Fathoms_of_Ego_2_BG.png",
"backgrounds/Story_Front_Gates_of_Daguanyuan,_Past_BG.png","backgrounds/Story_Tiekan_Temple_4_BG.png",
"backgrounds/Story_Daguanyuan_-_Tubitang_3_BG.png","backgrounds/Story_Corridor_of_the_Thumb_BG.png",
"backgrounds/Story_The_House_of_Spiders_Rooftop_1_BG.png","backgrounds/Story_Corridor_of_the_Ring_1_BG.png","backgrounds/Story_Corridor_of_the_Ring_2_BG.png",
"backgrounds/Story_La_Manchaland_Front_Gates_BG.png","backgrounds/Story_A_Certain_Castle,_Past_2_BG.png",
"backgrounds/Story_Wuthering_Heights_Basement_2_BG.png","backgrounds/Story_K_Corp._Laboratory_Hallway_BG.png",
"backgrounds/Story_The_Old_Sinclair_Estate_2_BG.png","backgrounds/Story_Unending_Hill_of_Corpses_2_BG.png","backgrounds/Story_Lobotomy_Corporation_Drilling_Ship_Entrance_2_BG.png",
"backgrounds/Story_Front_of_Eunbong’s_Bar_&_Fryers_BG.png","backgrounds/Story_Wuthering_Heights_Garden_BG.png",
"backgrounds/Story_Screening_Room_3_BG.png","backgrounds/Story_The_Pallid_Whale's_Heart_2_BG.png","backgrounds/Battle_Erlking_Heathcliff_Rooftop_BG.png"]

charachter_list = ["charachters/Dante_StandingSprite.png",
"charachters/Don_Quixote_StandingSprite(1).png","charachters/Heathcliff_Remember_Sprite_7.png",
"charachters/Ryōshū_Scabbard_Sprite_2.png","charachters/Vergilius_Sprite_2.png","charachters/Gregor_StandingSprite.png"
,"charachters/Sinclair_Sprite_2.png","charachters/Hong_Lu_Baby_Sprite_13.png","charachters/Rien_Sprite_4.png",
"charachters/Meursault_StandingSprite.png","charachters/Wei_Sprite_3.png","charachters/Lucio_Sprite_1.png",
"charachters/Ryōshū_Detective_Sprite_3.png","charachters/Dongrang_Sprite_4.png","charachters/Jia_Xichun_StandingSprite.png","charachters/Outis_Sprite_14.png",
"charachters/Faust_StandingSprite.png","charachters/Catherine_Sprite_1.png","charachters/Yi_Sang_Sprite_17.png",
"charachters/Hong_Lu_Past_StandingSprite.png","charachters/Faust_AF_2025_Sprite_3.png","charachters/Valencina_Sprite_6.png",
"charachters/Don_Quixote_Sancho_StandingSprite.png","charachters/La_Manchaland's_Don_Quixote_Past_StandingSprite.png",
"charachters/Camille_Sprite_1.png","charachters/Rodion_Sprite_4.png","charachters/Erlking_Heathcliff_StandingSprite.png",
"charachters/A_Certain_Sinclair_Sprite_5.png","charachters/Hong_Lu_Sprite_5.png","charachters/Lei_Heng_Sprite_1.png",
"charachters/Charon_2_StandingSprite.png","charachters/Ishmael_StandingSprite.png","charachters/Kromer_StandingSprite.png",
"charachters/Jia_Qiu_Sprite_4.png","charachters/Every_Catherine_Sprite_1.png","charachters/Jia_Mu_StandingSprite.png","charachters/Jia_Mu_Sprite_7.png",
"charachters/Ahab_Sprite_4.png","charachters/Gregor_Roach_Emperor_StandingSprite.png","charachters/Ricardo_Sprite_4.png"]


selected_characher = random.choice(charachter_list)
slected_background = random.choice(background_list)

#background imag 
bg_image = PIL.Image.open(slected_background)

bg_photo = PIL.ImageTk.PhotoImage(bg_image)


background = ttk.Label(root, image=bg_photo, borderwidth=0)
background.place(x=-400, y=-400, width=1500, height=1500)

# dante limbus company



#my button <3, i love him like my son
def toggle_script():
    global Script_Running,exploring, battling

    Script_Running = not Script_Running

    if Script_Running:
        toggle_btn.config(text="Script ON", bootstyle="success")
        battling = True
    else:
        toggle_btn.config(text="Script OFF", bootstyle="danger")
        exploring = False
        battling = False

toggle_btn = ttk.Button(
    root,
    text="Script OFF",
    bootstyle="danger",
    command=toggle_script
)
toggle_btn.pack(pady=10)

#bum vibe code snippet, why wont he be invisible!!!!
# make a particular colour (here white) completely transparent

#chat gpt save me and my life is yours :praying emoji: :crying emoji:

dante = PIL.Image.open(selected_characher).convert("RGBA")
dante = dante.resize((400, 400))
dante_img = PIL.ImageTk.PhotoImage(dante)


dante_label = tk.Label(root, image=dante_img, borderwidth=0)
dante_label.place(x=50, y=200)
dante_label.image = dante_img


#print("script start")


def upd_label():
    global dante_img        # we will reassign it
    global glow_index

    if battling and winrate_just_found:
        label.configure(text="State: Winrate Found! 🤤",
                        font=("Consolas", 16, "bold"),
                        foreground=glow_colors[glow_index])
        sprite_path = "son quihote images/Don_Quixote_Sprite_15.png"
        glow_index = (glow_index + 1) % len(glow_colors)
    elif battling and victory_just_found:
        label.configure(text="Battle Finished! 🥳",
                        font=("Consolas", 16, "bold"),
                        foreground="#ffd166")

    elif battling:
        label.configure(text="State: Battling 🗡️",
                        font=("Consolas", 16, "bold"),
                        foreground="#c52400")

    elif exploring:
        label.configure(text="State: Exploring 🎲",
                        font=("Consolas", 16, "bold"),
                        foreground="#aaaaaa")

    else:
        label.configure(text="State: Idle 🕒", foreground="#888888")


    # update the canvas image
    #dante_guy.itemconfig(dante_image_id, image=dante_img)

    root.after(1000, upd_label)

label = ttk.Label(
    root,
    text="State: Idle",
    font=("Arial", 16),
    bootstyle="secondary",       # choose a colour/style instead of bg
    relief="groove",
    borderwidth=2,
    padding=(10, 5)              # replaces padx/pady
)
label.pack(pady=10)


def char_change():
    global selected_characher, dante_img, dante_label
    selected_characher = random.choice(charachter_list)

    dante = PIL.Image.open(selected_characher).convert("RGBA")
    dante = dante.resize((400, 400))
    dante_img = PIL.ImageTk.PhotoImage(dante)

    dante_label.configure(image=dante_img)
    dante_label.image = dante_img

def bg_change():
    global slected_background, bg_photo, background
    slected_background = random.choice(background_list)
    bg_image = PIL.Image.open(slected_background)
    bg_photo = PIL.ImageTk.PhotoImage(bg_image)
    
    background.configure(image=bg_photo)
    background.image = bg_photo

char_button = ttk.Button(root,text = "change charachter",command=char_change, bootstyle="light")
bg_button = ttk.Button(root,text = "change background",command=bg_change, bootstyle="light")

char_button.pack(anchor="e")
bg_button.pack(anchor="e")

#i fixed bugs with chat gpt :( sorry , i lowk made this loop though, i just messed up the order anc
#chat fixed it.
def explore_and_battle_loop():
    #you know i mad this because it doesn have obnoxious hashtags.
    global battling, exploring, entered_room_just_found, victory_just_found
    with mss.mss() as sct:
        monitor = sct.monitors[1]


        while True:  # main loop
            
            if not Script_Running:
                time.sleep(0.3)
                continue




            img = np.array(sct.grab(monitor))
            gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)


            #nevermind i used chat gpt to make it work/look cleaner.


            # =====================
            # BATTLE STATE <---chat gpt slop :(
            # =====================
            if battling:
                #print("battle start")

                # ---- Check for Victory FIRST ----
                result = cv2.matchTemplate(gray, Victory, cv2.TM_CCOEFF_NORMED)
                _, victory_val, _, _ = cv2.minMaxLoc(result)

                if victory_val >= threshold:
                    #print("Victory found!", victory_val)
                    battling = False
                    exploring = True
                    victory_just_found = False
                    time.sleep(0.3)
                    continue

                # ---- Then check for Winrate ----
                result = cv2.matchTemplate(gray, winrate, cv2.TM_CCOEFF_NORMED)
                _, winrate_val, _, _ = cv2.minMaxLoc(result)

                if winrate_val >= threshold:
                    #print("Winrate found!", winrate_val)
                    pydirectinput.press("p")
                    time.sleep(0.3)
                    pydirectinput.press("enter")
                    time.sleep(0.3)

            # =====================
            # EXPLORING STATE
            # =====================
            elif exploring:
                #print("exploring")

                if not entered_room_just_found:
                    result = cv2.matchTemplate(gray, enter_room, cv2.TM_CCOEFF_NORMED)
                    _, max_val, _, max_loc = cv2.minMaxLoc(result)

                    if max_val >= threshold:
                        center_x = max_loc[0] + w3 // 2
                        center_y = max_loc[1] + h3 // 2
                        pydirectinput.moveTo(center_x, center_y)
                        pydirectinput.click()

                        entered_room_just_found = True
                        time.sleep(.2)

                else:
                    result = cv2.matchTemplate(gray, to_battle, cv2.TM_CCOEFF_NORMED)
                    _, max_val, _, max_loc = cv2.minMaxLoc(result)

                    if max_val >= threshold:
                        center_x = max_loc[0] + w4 // 2
                        center_y = max_loc[1] + h4 // 2
                        pydirectinput.moveTo(center_x, center_y)
                        pydirectinput.click()

                        exploring = False
                        battling = True
                        entered_room_just_found = False
                        time.sleep(.2)

            time.sleep(0.02)
#chud programmer looks like hes larping (vibecoding in big 2026)


upd_label() 
threading.Thread(target=explore_and_battle_loop, daemon=True).start()

root.mainloop()

#on 3/9/2026 i sharded manager don and got sweet aroma ryoshu from a single pull
#im so lucky, thanks to this script


#this runs like shit, optomize your script NOW


#3/10/2026 i tried to vibecode my way to transparent png images(don quihote) i added useless ai slop instead damn...
#the white looks ugly but it is whatever :( at leats it works...