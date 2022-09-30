# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:36:13 2022

@author: Laboratorio
"""

"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream
import pygame

pygame.init()

x_max = 1500
y_max = 1000
win   = pygame.display.set_mode((x_max,y_max))

# Avatar parameters
x1             = 250
y              = y_max/2
radius         = 100
vel_x, vel_y   = (10, 5)
jump           = False
run            = True
threshold      = 1.0
beta = 0

# Init EEG streaming via LSL
print("Procurando o sinal EEG...")
streams_eeg    = resolve_stream('type', 'signal')
inlet_eeg      = StreamInlet(streams_eeg[0])



while run:
  win.fill((0, 0, 0))
  pygame.draw.circle(win, (255*beta*vel_x/x_max, 255*beta*vel_x/x_max, 255), (int(x1), int(y_max/2)), radius)
  sample_eeg, time_ov_  = inlet_eeg.pull_sample(0)  # Sinal EEG
  
  if sample_eeg:    

    beta = sample_eeg[0]
    print(beta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()
    
    if beta > threshold:
        x1 += beta*vel_x
    if x1 > x_max:
        x1 = 0
            
     # if jump is False and userInput[pygame.K_SPACE]:
     #    jump = True

     # if jump is True:
     #     y -= vel_y
     #     vel_y -= 1
     #     if vel_y <-10:
     #         jump = False
     #         vel_y = 10

    pygame.display.update()