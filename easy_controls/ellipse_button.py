#!/usr/local/bin/python
# -*- coding: utf-8 -*-
            
class Ellipse_button(object):
    def __init__(self):
        self.color1 = color(0)
        self.color2 = color(0)
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.click = False
        self.tdist = 0
        
    def custom(self, x1, y1, w1, col1 = '#C62002', col2 = '#0BA00C'):
        self.x = x1
        self.y = y1
        self.w = w1
        self.h = w1
        self.color1 = col1
        self.color2 = col2
        self.tdist = self.w / 2
        
    def show(self, tx, ty):
        if dist(tx, ty, self.x, self.y) <= self.tdist:
            fill(self.color2)
        else:
            fill(self.color1)
        ellipseMode(CENTER)
        ellipse(self.x, self.y, self.w, self.h)
            
    def pressed(self, tx, ty, button = 'any'):
        if button != 'any':
            if dist(tx, ty, self.x, self.y) <= self.tdist and mouseButton == button:
                return True
            else:
                return False
        else:
            if dist(tx, ty, self.x, self.y) <= self.tdist and mousePressed:
                return True
            else:
                return False
