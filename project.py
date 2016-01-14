#!/usr/bin/env python
 
"""
url: http://thepythongamebook.com
licence: gpl, see http://www.gnu.org/licenses/gpl.html
author: Ching Yuen Ng / Aaron Schwartz
"""
 
####
 
import pygame as pyg
import time
import random as rand
import math
import string
 
#### configuration

#text####################################################

############################################################

'''
Remember....
    Reset stack on level complete
    hardcode languages / levels
    compare stack w/ ans stack
    add history tracker
    compare history tracker
    
'''






######images#############################################
fire=pyg.image.load('fire.png')
water=pyg.image.load('water.png')
mage=pyg.image.load('mage17.png')
firedoor=pyg.image.load('firedoor38.png')
waterdoor=pyg.image.load('waterdoor38.png')
popdoor=pyg.image.load('pop38.png')
nothingdoor=pyg.image.load('nothingdoor38.png')
floor=pyg.image.load('floor33.png')
start=pyg.image.load('start.png')
wall=pyg.image.load('wall33.png')
manabar=pyg.image.load('manabar.png')
title=pyg.image.load('title.png')
small_fire=pyg.image.load('small_fire.png')
small_water=pyg.image.load('small_water.png')
scroll=pyg.image.load('scroll.png')
lvl1=pyg.image.load('lvl1.png')
endscreen=[lvl1]


def draw_image(png_file,x,y):
    shade=pyg.display.get_surface()
    picture_size=(20,20)
    picture_tiles = [pyg.Rect((0,0), picture_size),
                     pyg.Rect((20,0), picture_size),
                     pyg.Rect((0,20), picture_size),
                     pyg.Rect((20,20), picture_size)]
    shade.blit(png_file,[x,y])




########################################################










###########################################################
stack=['E','E','E','E','E','E','E','E','E','E','E','E','E']
history = []

current_input=['E','E','E','E','E','E','E','E','E','E','E','E','E']
current_live=0
pointer= [0]
level = [1]
P_Lives = [0]

'''
   ANSWERS MUST BE IN A LIST

'''



#level 1
#lang = #of fire equal #of water
input1=['F','W','W','W','F','F']
#ans for level 1
life1=6
ans1=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans1_history1=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans1_history2=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans1_history3=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans1_history4=['W','W','E','E','E','E','E','E','E','E','E','E','E']
ans1_history5=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans1_history6=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans1_history=[ans1_history1,ans1_history2,ans1_history3,ans1_history4,ans1_history5,ans1_history6]



#level 2
#lang = #of fire is more than water
input2=['F','W','F','W','W','F','W','F','F','F']
#ans for #of fire is more than water
life2=10
ans2=['F','F','E','E','E','E','E','E','E','E','E','E','E']

ans2_history1=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history2=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history3=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history4=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history5=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history6=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history7=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history8=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history9=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans2_history10=['F','F','E','E','E','E','E','E','E','E','E','E','E']
ans2_history=[ans2_history1,ans2_history2,ans2_history3,ans2_history4,ans2_history5,ans2_history6,\
              ans2_history7,ans2_history8,ans2_history9,ans2_history10]

#level 3
#lang = fire^i and water^j given that i!=j
input3=['F','W','F','W','W','F','W','F','W','W']
life3=10
ans3=['W','W','E','E','E','E','E','E','E','E','E','E','E']

ans3_history1=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history2=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history3=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history4=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history5=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history6=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history7=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history8=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history9=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans3_history10=['W','W','E','E','E','E','E','E','E','E','E','E','E']

ans3_history=[ans3_history1,ans3_history2,ans3_history3,ans3_history4,ans3_history5,ans3_history6,\
              ans3_history7,ans3_history8,ans3_history9,ans3_history10]

#level 4
#lang = fire is at least 3 more than water
input4=['F','W','W','W','F','F','F','F','W','F','F']
life4=11
ans4=['F','F','W','E','E','E','E','E','E','E','E','E','E']

ans4_history1=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans4_history2=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans4_history3=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans4_history4=['W','W','E','E','E','E','E','E','E','E','E','E','E']
ans4_history5=['W','E','E','E','E','E','E','E','E','E','E','E','E']
ans4_history6=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans4_history7=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans4_history8=['F','F','E','E','E','E','E','E','E','E','E','E','E']
ans4_history9=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans4_history10=['F','F','E','E','E','E','E','E','E','E','E','E','E']
ans4_history11=['F','F','W','E','E','E','E','E','E','E','E','E','E']

ans4_history=[ans4_history1,ans4_history2,ans4_history3,ans4_history4,ans4_history5,ans4_history6,\
              ans4_history7,ans4_history8,ans4_history9,ans4_history10,ans4_history11]

#level 5
#lang = there is a water after a fire
input5=['W','W','W','F','F','F','W']
life5=7
ans5=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_2=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_3=['F','F','E','E','E','E','E','E','E','E','E','E','E']
    
ans5_history1=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_history2=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_history3=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_history4=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_history5=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_history5_2=['F','F','E','E','E','E','E','E','E','E','E','E','E']
ans5_history6=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_history6_2=['F','F','E','E','E','E','E','E','E','E','E','E','E']
ans5_history6_3=['F','F','F','E','E','E','E','E','E','E','E','E','E']
ans5_history7=['E','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_history7_2=['F','E','E','E','E','E','E','E','E','E','E','E','E']
ans5_history7_3=['F','F','E','E','E','E','E','E','E','E','E','E','E']

ans5_history=[ans5_history1,ans5_history2,ans5_history3,ans5_history4,ans5_history5,ans5_history6,ans5_history7]



final_input=[input1,input2,input3,input4,input5]
final_history=[ans1_history,ans2_history,ans3_history,ans4_history,ans5_history]
final_ans=[ans1,ans2,ans3,ans4,ans5]



def current_input_update(current_input,level,final_input):
    i=0
    while i < len((final_input[level[0]-1])):
        current_input[i]=(final_input[level[0]-1])[i]
        i+=1







def P_LivesDecrease(lives):
    P_Lives[0] = P_Lives[0] - 1

def draw_stack(stack):
    #c=pyg.time.Clock()
    i=0
    x=712
    y=515
    while i<13:
        if stack[i] == 'F':
            draw_image(fire,x,y)
            i+=1
            y-=39
            
        elif stack[i] == 'W':
            draw_image(water,x,y)
            i+=1
            y-=39
            
        else:
            #draw_image(flush,x+4,y)
            #draw_image(start,x+2,y+9)
            i+=1
            y-=39
    
def stack_reset(stack):
    i=0
    while i < 12:
        stack[i]='E'
        i+=1

def stack_mod(stack,action):
    i=12
    if action=='P':
        while i>=0:
            if stack[i]=='E':
                i-=1
            else:
                stack[i]='E'
                break
    
    if action=='F':
        while i>=0:
            if stack[0] == 'E':
                stack[0]='F'
                break
            if stack[i] =='E' and stack[i-1]!= 'E':
                stack[i]='F'
                break
            else:
                i-=1
    if action=='W':
        while i>=0:
            if stack[0]=='E':
                stack[0]='W'
                break
            if stack[i] =='E' and stack[i-1]!= 'E':
                stack[i]='W'
                break
            else:
                i-=1


#max stack will be 17 elements
def check_stack(map):
    stack=[]
    i=1
    while i < 18:
        if (map[i])[24]=='.':
            i=i+1
            pass
        else:
            stack.append((map[i])[24])
            i=i+1
    return stack


mapcolors =\
{'x': (100, 60, 30),
 'd': (30, 120, 10),
 'u': (30, 190, 10),
 'r': (250, 250, 0),
 'e': (250, 0, 0),
 'f': (0,0,0),
 'w': (0,0,0),
 'F': (0,0,0),
 'W': (80, 0, 250),
 'P': (0,0,0),
 'N': (250,250,250)}
 
config =\
{'fullscreen': False,
 'visibmouse': False,
 'width': 800,
 'height': 600,
 'back_color': (0, 0, 0),
 'font_ratio': 15,
 'font_color': (255, 255, 255),
 'fps': 100,
 'dt': 0.01,
 'friction': 0.987,
 'player_sizefac': 1.2,
 'player_color': (0, 0, 255),
 'player_accel': 400,
 'width_sensors': 8,
 'height_sensors': 8,
 'title': "The Mage's Puzzle" "(move with arrow keys)",
 'waiting_text': "quit=Esc, again=Other Key",
 'menu_text': "",
 'help_text': "",
 'winning_text': "You escaped the dungeon!  Enter to return.",
 'losing_text': "Despite your efforts, you could not escape...  Enter to return"}


#### maps
# x = wall
# s = start
# d = level down
# u = level up
# r = random level

####New Doors
# F = StackFire door
# W = StackWater door
# P = StackPop door
# N = StackNothing door


# 26 x 19
hardmap =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs.............x.....x.xkx",
 "xxxx..xx..xxx..x..x..x.xkx",
 "x..........x......x....xkx",
 "x..xxx.....x..xxxxx...xxkx",
 "x..x...............N...xkx",
 "x..x...xxxx.x..x.......xkx",
 "x....x......x..xxxx..x.xkx",
 "xxx..x..P...x..x.......xkx",
 "x....xxxxx.xx..x..x....xkx",
 "x.F......x........x....xkx",
 "x............x..xxxx...xkx",
 "xx...xxx...........x...xkx",
 "x....x....xxxxx........xkx",
 "x..xxxx...x..x..x...x..xkx",
 "x............x..x.W.x..xkx",
 "xxxxxxx..x...x..x...x..xkx",
 "x........x...x.........xkx",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]

hardmap2 =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs.............x.....x.xkx",
 "xxxx..xx..xxx..x..x..x.xkx",
 "x..........x......x....xkx",
 "x..xxx.....x..xxxxx...xxkx",
 "x..x...............N...xkx",
 "x..x...xxxx.x..x.......xkx",
 "x....x......x..xxxx..x.xkx",
 "xxx..x..P...x..x.......xkx",
 "x....xxxxx.xx..x..x....xkx",
 "x.F......x........x....xkx",
 "x............x..xxxx...xkx",
 "xx...xxx...........x...xkx",
 "x....x....xxxxx........xkx",
 "x..xxxx...x..x..x...x..xkx",
 "x............x..x.W.x..xkx",
 "xxxxxxx..x...x..x...x..xkx",
 "x........x...x.........xkx",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]

hardmap3 =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs......xNxxx...x...x..xkx",
 "xxxx.x..x.......xx.....xkx",
 "x....x..xxxxxx..x..xx..xkx",
 "x..x.x.......x..x..x..xxkx",
 "xx.xxx...x...x.....x...xkx",
 "x.......xxx..x.xxxxxx..xkx",
 "xxxxxx...x...xxx..Wx...xkx",
 "x......x...x.....xxx.x.xkx",
 "x.x.xxxx..xx.x...x.....xkx",
 "x.x...x......x...xx.x.xxkx",
 "x.xxx.x.xxx..xx..x.....xkx",
 "x.x.x.xxx...xx...x.x.x.xkx",
 "x...x...xx...x..xx.....xkx",
 "xx.xx......x.x..Px.xxxxxkx",
 "x..x...xxx.x...xxx....xxkx",
 "x..xxxxxFx.xxxxx.xxxx..xkx",
 "x........x.............xkx",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]

hardmap4 =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs..x......x.x.........xkx",
 "xxx.x.xxxx...xxxxx..xx.xkx",
 "x...x.x..xxxxx...x...x.xkx",
 "x...x..F.....x.....x.x.xkx",
 "x...xxx.....xx.....x.x.xkx",
 "x.....xxx..xx..N.....x.xkx",
 "x...x.......x..x..x..x.xkx",
 "x..xx....xx.xxx.xxxx.x.xkx",
 "xx..x.x..x....x..x...x.xkx",
 "x..xxxWxxx..x.xx.x..x..xkx",
 "xx..xx.................xkx",
 "x..xx.xxxxx.xxxxxx..xx.xkx",
 "xx..x.....x...x........xkx",
 "x..xx.....x..P..xxxx...xkx",
 "xx..x..x..xxxxx.x..x...xkx",
 "x...x....x...x.........xkx",
 "x.x...x....x...x...xx..xkx",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]

easymap =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs......x....x......x..xkx",
 "xxxx.......x..x...N....xkx",
 "x.......x....x.....xx..xkx",
 "x.......xxxxxxxxx......xkx",
 "x.........x.....x..x.x.xkx",
 "x....x..........x......xkx",
 "x....xxxxx.xxx..x.xx...xkx",
 "x........x.x....x....x.xkx",
 "x...x....xx..xxxx.x.x..xkx",
 "x...x....x.............xkx",
 "x...x....x.......x.P.x.xkx",
 "x........x.xxxx........xkx",
 "x.....x....x.Wx...x.x..xkx",
 "x..x..x.......x........xkx",
 "x..xxxxx....xxxxxxx....xkx",
 "x......x....x.....x....xkx",
 "x.....Fx...............xkx",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]

easymap2 =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs....x...........x....xkx",
 "xxxx..x..x..x.x...x.x..xkx",
 "x.....x..x........x.x..xkx",
 "x.........xxxx......x..xkx",
 "x...xx.......x..x......xkx",
 "x.......x.......x......xkx",
 "x....x....N.....xxx....xkx",
 "x.x.....x..x...........xkx",
 "x....x.......xP.....xx.xkx",
 "x......W.x.............xkx",
 "x..........x...........xkx",
 "x..x........F..xxxxx...xkx",
 "x................x.xx..xkx",
 "x....x.....x.....x.....xkx",
 "x.......x......xxx..x..xkx",
 "x..xx...x...xx.....xx..xkx",
 "x...x...x.......xx.....xkx",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]

divemap =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs...x.........x...P...xkx",
 "x....x.xxx.x...x.x...x.xkx",
 "xx...x.....x...x.....x.xkx",
 "x..x.x.x.....x.x..x.x..xkx",
 "x....xx..x.x..........Fxkx",
 "x.x.xx.....xx..x..x....xkx",
 "x....x..x..x...x....x..xkx",
 "x..x.x...x.x..xxxxxxxxxxkx",
 "x.x..xx....x...x...N...xkx",
 "x..........xx..x..x..x.xkx",
 "x.x..x....xx...x.......xkx",
 "x..x.x.x...x...xW...x..xkx",
 "xxx..x...x.x.x.x.......xkx",
 "x....x.....x...x..x..x.xkx",
 "x..xxxx.......xxx..x...xkx",
 "x.x........xx..x.....x.xkx",
 "x....x.....x.......x...xkx",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]

# game maps
maps =  hardmap, hardmap3, hardmap4, easymap, easymap2, divemap


#### map constants
 
UP = 1
DOWN = -1
RANDOM = -2
START = -3
PLACES = set(('u', 'd', 'r', 'e', 'F', 'W', 'P', 'N'))
NOT_DRAWABLES = set(('.', 's', 'f','w','F', 'W', 'P', 'N','k', 'x'))
 
####
 
class PygView(object):
  """Pygame interface"""
 
  CURSORKEYS = slice(273, 277)
  BACKKEYS = pyg.K_BACKSPACE
  ENTERKEYS = pyg.K_RETURN
  SPACEKEYS = pyg.K_SPACE
  LEVEL1 = pyg.K_1
  LEVEL2 = pyg.K_2
  LEVEL3 = pyg.K_3
  LEVEL4 = pyg.K_4
  LEVEL5 = pyg.K_5
  QUIT_KEYS = pyg.K_ESCAPE, pyg.K_q,
  EVENTS = 'up', 'down', 'right', 'left'
 
  def __init__(self, controller, config):
 
    self.controller = controller
    self.width = config.width
    self.height = config.height
    self.back_color = config.back_color
    self.fps = config.fps
    self.font_color = config.font_color
 
    pyg.init()
    flags = pyg.DOUBLEBUF | [0, pyg.FULLSCREEN][config.fullscreen]
    self.canvas = pyg.display.set_mode((self.width, self.height), flags)
    pyg.display.set_caption(config.title)
    self.clock = pyg.time.Clock()
    pyg.mouse.set_visible(config.visibmouse)
    self.font = pyg.font.Font(None, self.height // config.font_ratio)
 
    
 
  @property
  def frame_duration_secs(self):
 
    return 0.001 * self.clock.get_time()
 
 
  def run(self):
    """Main loop"""
 
    running = True
    while running:
      self.clock.tick_busy_loop(self.fps) 
      running = self.controller.dispatch(self.get_events())
      self.flip()
    else:
      self.quit()
 
    ###############
  def get_events(self):
 
    keys = pyg.key.get_pressed()[PygView.CURSORKEYS]
    move_events = [e for e, k in zip(PygView.EVENTS, keys) if k]
 
    for event in pyg.event.get():
      if event.type == pyg.QUIT:
        return 'quit', move_events
      if event.type == pyg.KEYDOWN:
        #select level from 1 to 4
        if event.key == PygView.LEVEL1:
            
        
            return 'level1', move_events
        if event.key == PygView.LEVEL2:
            return 'level2', move_events
        if event.key == PygView.LEVEL3:
            return 'level3', move_events
        if event.key == PygView.LEVEL4:
            return 'level4', move_events
        if event.key == PygView.LEVEL5:
            return 'level5', move_events
        if event.key == PygView.BACKKEYS:
          return 'menu', move_events
        if event.key == PygView.ENTERKEYS:
          return 'enter', move_events
        if event.key == PygView.SPACEKEYS:
          return 'help', move_events
        if event.key in PygView.QUIT_KEYS:
          return 'quit', move_events
        else:
          return 'other_key', move_events
      
    else:
      return None, move_events
 
 
  def rectangle(self, xywh, color, border=0):
 
    pyg.draw.rect(self.canvas, color, xywh, border)
 
 
  def draw_text(self, text):
 
    fw, fh = self.font.size(text)
    surface = self.font.render(text, True, self.font_color)
    self.canvas.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))
 
 
  def flip(self):
 
    pyg.display.flip()
    self.canvas.fill(self.back_color) 
 
 
  def quit(self):
 
    pyg.quit()
 
####
 
class Grid(object):
  """Calculate points on a rectangular grid."""
 
  def __init__(self, dx=1, dy=1, xoff=0, yoff=0):
 
    self.dx = dx
    self.dy = dy
    self.xoff = xoff
    self.yoff = yoff
 
 
  def get_point(self, x, y):
 
    return self.xoff + x * self.dx, self.yoff + y * self.dy
 
 
  def get_rect(self, x, y):
    """Return rectangle parameters for pygame."""
 
    return self.get_point(x, y) + (self.dx, self.dy)
 
 
  def get_cell(self, x, y):
    """Snap coordinates to center point grid."""
    x = int(x+0.5)
    y = int(y+0.5)
    return (x-self.xoff+self.dx//2)//self.dx, (y-self.yoff+self.dy//2)//self.dy
 
####
 
class Map(object):
  """Maze map representation""" 
 
  def __init__(self, map_data):
 
    self.width = len(map_data[0])
    self.height = len(map_data)
    self.data = map_data

 
 ######################################################################
  def __getitem__(self, (x, y)):
 
    return self.data[y][x]
 
 
  @property
  def start(self):
    """Search the starting point, there should be only one."""
 
    for i, y in enumerate(self.data):
      for j, x in enumerate(y):
        if x == 's':
          return j, i

 
####
 
class Mapper(object):
  """Manage all maps."""
 
  def __init__(self, maps, width, height):
 
    self.view_width = width
    self.view_height = height
    self.maps = [Map(m) for m in maps]
    self.bool = 1
  
  
  
 
  def select(self, mode=START):
 
    assert mode in (START, UP, DOWN, RANDOM), "wrong selection"
 
    n = len(self.maps)
    if mode == START:
      self.act_index = 0
    elif mode == RANDOM:
      if len(self.maps) > 1:
        self.act_index = rand.choice(list(set(xrange(n)) - set((self.act_index,))))  
    else:
      self.act_index = (self.act_index + n + mode) % len(self.maps)
 
    self.act_grid, self.act_center_grid = self.adjust_grids()
    return self.act_map, self.act_grid, self.act_center_grid
 
 
  def adjust_grids(self):
    """There are 2 sorts of grids:
    a grid for the upper left Corner for drawing rectangles,
    a grid for their center points, which are used for collision detection."""
 
    smap = self.act_map
    w = self.view_width // smap.width - 1
    h = self.view_height // smap.height - 1
    xoff = self.view_width - smap.width * w 
    yoff = self.view_height - smap.height * h
    grid = Grid(w, h, xoff//2, yoff//2)
    # +1 !
    center_grid = Grid(w, h, xoff//2 + w//2 + 1, yoff//2 + h//2 + 1)
 
    return grid, center_grid
 
 
  def draw_map(self, view):
 
    smap = self.act_map
    grid = self.act_grid
    width = smap.width
      
    for y in xrange(smap.height):
      for x in xrange(width):
        place = smap[x, y]
        if 'F' in place:
          co=grid.get_rect(x,y)
          draw_image(floor,co[0]-3,co[1])
          draw_image(firedoor,co[0]-8,co[1]-8)
        if 'W' in place:
          co=grid.get_rect(x,y)
          draw_image(floor,co[0]-3,co[1])
          draw_image(waterdoor,co[0]-8,co[1]-8)
        if 'P' in place:
          co=grid.get_rect(x,y)
          draw_image(floor,co[0]-3,co[1])
          draw_image(popdoor,co[0]-8,co[1]-8)
        if 'N' in place:
          co=grid.get_rect(x,y)
          draw_image(floor,co[0]-3,co[1])
          draw_image(nothingdoor,co[0]-8,co[1]-8)
        if '.' in place:
          co=grid.get_rect(x,y)
          draw_image(floor,co[0]-3,co[1])
        if 's' in place:
          co=grid.get_rect(x,y)
          draw_image(start,co[0]-3,co[1])
        if 'x' in place:
          co=grid.get_rect(x,y)
          draw_image(wall,co[0]-3,co[1])
        if 'k' in place:
          co=grid.get_rect(x,y)
          draw_image(manabar,co[0]-3,co[1])
        if 'f' in place:
            co=grid.get_rect(x,y)
            draw_image(fire,co[0]-4,co[1]-10)
        if 'w' in place:
            co=grid.get_rect(x,y)
            draw_image(water,co[0]-4,co[1]-10)
        if place not in NOT_DRAWABLES:
          view.rectangle(grid.get_rect(x, y), mapcolors[place], place in PLACES)
  
    draw_stack(stack)
    
    
  

#####################
    
  @property
  def act_map(self):
 
    return self.maps[self.act_index]
 
 
  @property
  def start(self):
 
    return self.act_map.start
 
 
  def get_point(self, x, y):
 
    return self.act_grid.get_point(x, y)
 
 
  def get_rect(self, x, y):
 
    return self.act_grid.get_rect(x, y)
 
 
  def get_cell(self, x, y):
 
    return self.act_center_grid.get_cell(x, y)
 
 
  @property
  def player_sizehint(self):
 
    return self.act_grid.dx // 2, self.act_grid.dy // 2
 
 ####
 
class Player(object):
  """Representation of the moving player rectangle"""
 
  dirs = {'up': (0, -1),
          'down': (0, 1),
          'left': (-1, 0),
          'right': (1, 0)}
 
  sensor_pts = ((0, 0), (1, 0), (1, 1), (0, 1))
 
  def __init__(self, x, y, width, height, color):
 
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.width2 = width // 2
    self.height2 = height // 2
    self.color = color
    self.dx = 0
    self.dy = 0
 
 
  @property
  def pos(self):
 
    return self.x, self.y
 
 
  @property
  def oldpos(self):
 
    return self.xold, self.yold
 
 
  def restore_pos(self):
 
    self.x, self.y = self.oldpos
 
 
  @property
  def center(self):
 
    x, y = self.pos
    return x + self.width2, y + self.height2
 
 
  def move(self, dt, friction):
 
    self.dx *= friction
    self.dy *= friction
    self.xold, self.yold = self.pos
    self.x += self.dx * dt
    self.y += self.dy * dt
 
 
  def accelerate(self, direct, acc):
 
    xdir, ydir = Player.dirs[direct]
    self.accx = xdir * acc
    self.accy = ydir * acc
    self.dx += self.accx
    self.dy += self.accy
 
 
  @property
  def vertex_sensors(self):
 
    x, y = self.pos
    return [(x + sx * self.width, y + sy * self.height) for sx, sy in Player.sensor_pts]
 
 
  def north_sensors(self, n):
 
    x, y = self.pos
    delta = self.width // n
    return [(x + i * delta, y) for i in xrange(1, n)]
 
 
  def south_sensors(self, n):
 
    x, y = self.pos
    delta = self.width // n
    h = y + self.height
    return [(x + i * delta, h) for i in xrange(1, n)]
 
 
  def west_sensors(self, n):
 
    x, y = self.pos
    delta = self.height // n
    return [(x, y + i * delta) for i in xrange(1, n)]
 
 
  def east_sensors(self, n):
 
    x, y = self.pos
    delta = self.height // n
    w = x + self.width 
    return [(w, y + i * delta) for i in xrange(1, n)]
 
 
  def bounce(self, west_east, north_south):
 
    self.dx = (self.dx, -(self.dx / 2))[west_east]
    self.dy = (self.dy, -(self.dy / 2))[north_south]
 
 
  def draw(self, view):
      
    
      
    current_input_update(current_input,level,final_input)

      
      
    #view.rectangle((self.x, self.y, self.width, self.height), self.color)
    draw_image(mage,self.x,self.y)
    
    if(current_input[pointer[0]]=='F'):
        draw_image(small_fire,self.x+1,self.y-15)
    
    if(current_input[pointer[0]]=='W'):
        draw_image(small_water,self.x,self.y-15)
  
      
    setText('Language:',100,20,(255,255,0), 30)
    setText('Lives Remaining: ' + str(P_Lives[0]), 550,560, (255,255,0), 30)

####

def setText(text,x,y,color,size):
    myfont=pyg.font.SysFont(None,size)
    screen=pyg.display.get_surface()
    label = myfont.render(text,1,color)
    screen.blit(label, (x,y))


# code for our menu




class Controller(object):
  """Global game control"""
 
  def __init__(self, view, maps, config):
 
    self.view = view(self, config)
    self.game = MazeGame(maps, config)
    self.game.reset(START)
    #self.state = 'playing'
    self.state = 'menu'
 
  def dispatch(self, all_events):
    """Control the game state."""
    event, move_events = all_events
      
    if self.state == 'menu':
      
      self.game.menu_wait(self.view)
      '''
      if event == 'enter':
          self.state='playing'
          self.game.reset(START)
          '''
      if event == 'help':
          self.state = 'help'
          self.game.help_wait(self.view)
      
      if event == 'level1':
          #pointer[0]=0
          level[0]=1
          P_Lives[0]=life1
          pointer[0]=0
         
         
          self.state = 'playing'
          self.game.reset(START)
      if event == 'level2':
          level[0]=2
          P_Lives[0]=life2
          pointer[0]=0
        
          self.state = 'playing'
          self.game.reset(START)
      if event == 'level3':
          level[0]=3
          P_Lives[0]=life3
          pointer[0]=0
        
          
          self.state = 'playing'
          self.game.reset(START)
      if event == 'level4':
          level[0]=4
          P_Lives[0]=life4
          pointer[0]=0
          
          
          self.state = 'playing'
          self.game.reset(START)

      if event == 'level5':
          level[0]=5
          P_Lives[0]=life5
          pointer[0]=0

          self.state = 'playing'
          self.game.reset(START)
    
    if self.state == 'help':
      self.game.help_wait(self.view)
      if event == 'menu':
         self.state = 'menu'
         self.game.menu_wait(self.view)
      if event == 'enter':
         self.state='playing'
         self.game.reset(START)
    
    
    
    #if self.state == 'level_complete':
    #self.game.level_complete_wait(self.view, 1, [])
        #(self.view,level,stack)
        
    if self.state == 'win':
      self.game.win_wait(self.view, level)
      if event == 'enter':
          self.state = 'menu'


    if self.state == 'lose':
      self.game.lose_wait(self.view)
      if event == 'enter':
          self.state = 'menu'
      
    
    if event == 'quit':
      self.game.quit()
      return False
 
    if self.state == 'playing':
      self.state = self.game.process(self.view, move_events)
      return True
 
    if self.state == 'ending':
      self.game.wait(self.view)
      if event == 'other_key':
        self.state = 'playing'
        self.game.reset(START)
 
    return True
 
 
  def run(self):
 
    self.view.run()
 
####
 
class MazeGame(object):
  """The actual game"""
 
  def __init__(self, maps, config):
 
    self.config = config
    self.dtimer = DeltaTimer(config.dt)
    self.mapper = Mapper(maps, config.width, config.height)
    self.player_accel= config.player_accel
    self.friction = config.friction


  def reset(self, mode):
 
    self.text = ""
    self.mapper.select(mode)
    x, y = self.mapper.get_point(*self.mapper.start)
    w, h =  self.mapper.player_sizehint
    size =  self.config.player_sizefac
    width = int(w * size)
    height = int(h * size)
    self.player = Player(x+1, y+1, width, height, self.config.player_color)
 
    
 
  def accelerate_player(self, events, accel):
 
    
    for ev in events:
      self.player.accelerate(ev, accel)
 
 
  def check_places(self):
    if(level[0]==1):
        current_input=input1
        history=final_history[0]
        setText('Fire and water mana are balanced',220,20,(255,255,0), 30)
  

    if(level[0]==2):
        current_input=input2
        history=final_history[1]
        setText('Fire mana is greater than water mana',220,20,(255,255,0), 30)
    
    if(level[0]==3):
        current_input=input3
        history=final_history[2]
        setText('Fire and water mana are unbalanced',220,20,(255,255,0), 30)
        
    
    if(level[0]==4):
        current_input=input4
        history=final_history[3]
        setText('There are at least 3 more fire mana than water mana',220,20,(255,255,0), 30)

    if(level[0]==5):
        current_input=input5
        history=final_history[4]
        setText('There is a water mana after a fire mana',220,20,(255,255,0), 30)
    
    




    
    
    
    
    place = self.mapper.act_map[self.mapper.get_cell(*self.player.center)]
    if place in PLACES:
      P_LivesDecrease(P_Lives[0])
    
      pointer[0]+=1
  
      if place == 'e':
        return 'ending'
      if place == 'F':
        stack_mod(stack,'F')
        
        if stack == (final_history[level[0]-1])[pointer[0]-1]:
          pass
        if stack != (final_history[level[0]-1])[pointer[0]-1]:
          stack_reset(stack)
          return 'lose'
        
        
        
        if P_Lives[0] <= 0:
          if stack == final_ans[level[0]-1]:
            stack_reset(stack)
            return 'win'
          if stack != final_ans[level[0]-1]:
            stack_reset(stack)
            return 'lose'

        else:
          self.reset({'u': UP, 'd': DOWN, 'r': RANDOM, 'F': UP, 'W': UP, 'P': UP, 'N': UP}.get(place))
      if place =='W':
        stack_mod(stack,'W')
        
        if stack == (final_history[level[0]-1])[pointer[0]-1]:
            pass
        if stack != (final_history[level[0]-1])[pointer[0]-1]:
            stack_reset(stack)
            return 'lose'
        
        
        
        if P_Lives[0] <= 0:
          if stack == final_ans[level[0]-1]:
            stack_reset(stack)
            return 'win'
          if stack != final_ans[level[0]-1]:
            stack_reset(stack)
            return 'lose'

        else:
          self.reset({'u': UP, 'd': DOWN, 'r': RANDOM, 'F': UP, 'W': UP, 'P': UP, 'N': UP}.get(place))
      if place =='P':
        stack_mod(stack,'P')
        
        if stack == (final_history[level[0]-1])[pointer[0]-1]:
            pass
        if stack != (final_history[level[0]-1])[pointer[0]-1]:
            stack_reset(stack)
            return 'lose'
        
        
        
        if P_Lives[0] <= 0:
            
          if stack == final_ans[level[0]-1]:
            stack_reset(stack)
            return 'win'
          if stack != final_ans[level[0]-1]:
            stack_reset(stack)
            return 'lose'

        else:
          self.reset({'u': UP, 'd': DOWN, 'r': RANDOM, 'F': UP, 'W': UP, 'P': UP, 'N': UP}.get(place))
      else:
          
        if stack == (final_history[level[0]-1])[pointer[0]-1]:
          pass
        if stack != (final_history[level[0]-1])[pointer[0]-1]:
          stack_reset(stack)
          return 'lose'
        
          
          
          
        if P_Lives[0] <= 0:
          if stack == final_ans[level[0]-1]:
            stack_reset(stack)
            return 'win'
          if stack != final_ans[level[0]-1]:
            stack_reset(stack)
            return 'lose'
            
        else:
          self.reset({'u': UP, 'd': DOWN, 'r': RANDOM, 'F': UP, 'W': UP, 'P': UP, 'N': UP}.get(place))
        
    
    return 'playing'
 
 
  def check_collision(self):
    """Check at first 4 sides of the player rectangle,
    if no collision occurs, check corners."""
 
    smap = self.mapper.act_map
    mapper = self.mapper
 
    ws = self.config.width_sensors
    hs = self.config.height_sensors
    north = [smap[mapper.get_cell(sx, sy)] == 'x'
             for sx, sy in self.player.north_sensors(ws)]
    south = [smap[mapper.get_cell(sx, sy)] == 'x'
             for sx, sy in self.player.south_sensors(ws)]
    east = [smap[mapper.get_cell(sx, sy)] == 'x'
             for sx, sy in self.player.east_sensors(hs)]
    west = [smap[mapper.get_cell(sx, sy)] == 'x'
            for sx, sy in self.player.west_sensors(hs)]
 
    west_east = any(west) or any(east)
    north_south = any(north) or any(south)
 
    if west_east or north_south:
      self.player.bounce(west_east, north_south)
      return True
 
    csx = False
    for sx, sy in self.player.vertex_sensors:
      if smap[mapper.get_cell(sx, sy)] == 'x':
        csx, csy = sx, sy
        break
 
    if not csx:
      return False
 
    old_px, old_py = self.player.oldpos
    px, py = self.player.pos
    old_csx = csx - px + old_px
    old_csy = csy - py + old_py
 
    old_cellx, old_celly = mapper.get_cell(old_csx, old_csy)
    cellx, celly = mapper.get_cell(csx, csy)
    self.player.bounce(abs(old_cellx - cellx) > 0, abs(old_celly - celly) > 0)
 
    return True
 
 
  def process(self, view, move_events):
    """Main method"""
 
    dur = view.frame_duration_secs
    #self.text = str(view.frame_duration_secs)
    self.accelerate_player(move_events, dur * self.player_accel)
    self.dtimer += dur
    self.dtimer.integrate(self.transform_player, self.friction)
 
    self.mapper.draw_map(view)
    self.player.draw(view)
    self.draw_text(view)
 

      
    return self.check_places()
 
 
  def transform_player(self, dt, friction):
    """Move player in 1 timestep dt."""
 
    self.player.move(dt, friction)  
    collision = self.check_collision()
    if collision:
      self.player.restore_pos()
      self.player.move(dt, friction)  
 
 
  def wait(self, view):
    """If player finds exit, ask for new game."""
 
    self.text = self.config.waiting_text
    self.draw_text(view)
 
        ###########################################
  def menu_wait(self,view):
    self.text = self.config.menu_text
    self.draw_text(view)
    draw_image(title,0,0)
    #setText("Mage Dungeon",200,200,(255,255,255),80)
    setText("Press 1-5 to select a level",250,400,(255,255,255),40)
    setText("Press space for help",270,450,(255,255,255),40)
    draw_image(scroll,100,50)
    
    
    
  def help_wait(self,view):
    self.text=self.config.help_text
    self.draw_text(view)
    #draw_image(title,0,0)
    setText("Press backspace to go back",100,25,(255,255,255),30)
    draw_image(firedoor,50,100)
    draw_image(waterdoor,50,200)
    draw_image(nothingdoor,50,300)
    draw_image(popdoor,50,400)
    setText("Channel fire into your mana pool",100,110,(255,255,255),40)
    setText("Channel water into your mana pool",100,210,(255,255,255),40)
    setText("Meditate - your mana pool is unchanged",100,310,(255,255,255),40)
    setText("Remove the last added mana from your pool",100,410,(255,255,255),40)
    setText("Use this to 'cancel' opposing elements",100,460,(255,255,255),40)
    
    setText("Each puzzle has a predefined path, with elements above the mage's head.",50,525,(255,255,0),25)
    setText("Each puzzle has an overlying theme above.  This can help you solve it!",50,550,(255,255,0),25)
  
  
  
  def win_wait(self,view, level):
    setText("You solved the puzle!", 300,500, (184,20,80),30)
    setText("Enter for main menu", 300,550, (184,20,80), 30)
    draw_image(endscreen[level[0] - 1], 50, 50)
  
  def lose_wait(self,view):
    setText("Despite your efforts, you could not escape...", 100,400, (24,184,80),30)
    setText("Enter for main menu",200,450,(24,184,80),30)
  
  
  
  def level_complete_wait(self,view, level, stack):
    if stack == final_ans[level -1]:
      self.text = self.config.winning_text
      setText("You escaped with your manapool!", 300,400, (184,20,80),30)
      draw_image(endscreen[level - 1], 100,100)
    else:
      self.text = self.config.losing_text
      setText("Despite your efforts, you could not escape...", 100,400, (24,184,80),30)
        ##qqqq

  def draw_text(self, view):
 
    view.draw_text(self.text)
 
 
  def quit(self):
 
    print "Bye"
 
####
 
class DeltaTimer(object):
  """Timing control"""
 
  def __init__(self, dt):
 
    self.dt = dt
    self.accu = 0.0
 
 
  def __iadd__(self, delta):
 
    self.accu += delta
    return self
 
 
  def integrate(self, func, *args):
    """For a fixed timestep dt, adjust movement to fps."""
    while self.accu >= self.dt:
      func(self.dt, *args)
      self.accu -= self.dt
 
####
 
class Config(object):
  """Change dictionary to object attributes."""
 
  def __init__(self, **kwargs):
 
    self.__dict__.update(kwargs)
 
####
 
def main():
 
  Controller(PygView, maps, Config(**config)).run()
  
 
####
 
if __name__ == '__main__':
 
  main()
