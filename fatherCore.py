#Monkey Butler - the Father

import random
import arcade
import os
import math
import turtle
import time
import requests
import json
import sys
from tkinter import *

#Measurements that sprites use to stay organized, usually sprite placement is based on every 10th of a screen width and 5.5th for height
screenWidth = 1920
screenHeight = 1080
centerX = screenWidth / 10
centerY = screenHeight - (screenHeight / 5.5)
spriteScaling = .45

#Math calculations for MB's speech sine wave

#Updates the weather
def update_weather():
    # Variables for Monkey Butler's weather detection system
    api_key = "c5bbe0c6b2d7ab5f9ae92a9441d47253"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Chadds Ford"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temp = y["temp"]
        current_pres = y["pressure"]
        current_hum = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
    else:
        print("I cannot find that city.")

    tempF = str(round(current_temp * 9/5-459.67))
    return tempF

#GUI Text color
guiColorCore = arcade.color.GREEN
guiColorDiscord = arcade.color.GRAY
guiColorMC = arcade.color.GREEN
guiColorSB = arcade.color.GRAY
guiColorLights = arcade.color.GRAY


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=False)

        self.player_list = None

        #Sounds and Voice Lines
        self.test_sound = arcade.load_sound("voice/test.mp3")
        #self.alex_sound = arcade.load_sound("voice/alex.mp3")
        self.I_Monkey_sound = arcade.load_sound("voice/I_Monkey.mp3")

        self.num_updates = 0
        self.text_string = ""

    def setup(self):

        #Sets up the MB image sprite
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("icons/butler2.png", spriteScaling)
        self.player_sprite.center_x = centerX
        self.player_sprite.center_y = centerY
        self.player_list.append(self.player_sprite)

        #Sets up the Discord status image sprite
        self.discord_list = arcade.SpriteList()
        self.discord_sprite = arcade.Sprite("icons/DL.png", spriteScaling/6)
        self.discord_sprite.center_x = centerX * 3
        self.discord_sprite.center_y = centerY
        self.discord_list.append(self.discord_sprite)

        #Sets up the MC Server status image sprite
        self.FGH_list = arcade.SpriteList()
        self.FGH_sprite = arcade.Sprite("icons/server.png", spriteScaling*1.3)
        self.FGH_sprite.center_x = centerX * 3
        self.FGH_sprite.center_y = centerY-196
        self.FGH_list.append(self.FGH_sprite)

        #Sets up the Space Bucket status image sprite
        self.SB_list = arcade.SpriteList()
        self.SB_sprite = arcade.Sprite("icons/bucket.png", spriteScaling*0.13)
        self.SB_sprite.center_x = centerX * 3
        self.SB_sprite.center_y = centerY-392
        self.SB_list.append(self.SB_sprite)

        #Sets up the lights status image sprite
        self.Lights_list = arcade.SpriteList()
        self.Lights_sprite = arcade.Sprite("icons/light.png", spriteScaling*0.69)
        self.Lights_sprite.center_x = centerX * 3
        self.Lights_sprite.center_y = centerY-588
        self.Lights_list.append(self.Lights_sprite)

        #Sets up the tiny thermometer image
        self.T_list = arcade.SpriteList()
        self.T_sprite = arcade.Sprite("icons/Thermometer.png", spriteScaling*0.35)
        self.T_sprite.center_x = 75
        self.T_sprite.center_y = centerY-190
        self.T_list.append(self.T_sprite)

    def on_draw(self):
        #Initiates render and draws background
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)

        #Draws the portrait border
        arcade.draw_rectangle_filled(centerX, centerY, 325, 325, guiColorCore)

        #Draws circle and Rectangle outline for discord icon
        arcade.draw_circle_filled(centerX*3, centerY, 75, guiColorDiscord)
        arcade.draw_rectangle_filled(centerX*4, centerY, 300, 100, guiColorDiscord)
        
        arcade.draw_circle_filled(centerX*3, centerY-196, 75, guiColorMC)
        arcade.draw_rectangle_filled(centerX*4, centerY-196, 300, 100, guiColorMC)
        
        arcade.draw_circle_filled(centerX*3, centerY-392, 75, guiColorSB)
        arcade.draw_rectangle_filled(centerX*4, centerY-392, 300, 100, guiColorSB)
        
        arcade.draw_circle_filled(centerX*3, centerY-588, 75, guiColorLights)
        arcade.draw_rectangle_filled(centerX*4, centerY-588, 300, 100, guiColorLights)
        
        #Labels
        #arcade.draw_text("Discord Status", centerX, centerY, arcade.color.BLUE, 24)

        #Draws MB's portrait in the top left.
        self.player_list.draw()

        #Draws various logos 
        self.discord_list.draw()
        self.FGH_list.draw()
        self.SB_list.draw()
        self.Lights_list.draw()
        self.T_list.draw()

        #Weather Variables
        if self.num_updates <= 0:
            self.text_string = update_weather() + " Fahrenheit"
            self.num_updates = 5400

        arcade.draw_text(self.text_string, 100, centerY - 210, arcade.color.GREEN, 28)

        #Gets the time in standard format
        localTime = time.strftime("%H:%M")

        if localTime == "13:00":
            arcade.play_sound(self.test_sound)
            time.sleep(61)
        #else:
            #print("not Time!")

        self.num_updates -= 1

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.I_Monkey_sound)


def main():
    window = MyGame(1900, 1060, "Monkey Butler Python-Integrated Graphical User Module Interface.py")
    window.setup()
    arcade.run()


main()
