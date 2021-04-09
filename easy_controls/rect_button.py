#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class Rect_button(object):
    def __init__(self):
        self.color1 = color(0)
        self.color2 = color(0)
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.click = False
        self.tx1 = 0
        self.ty1 = 0
        self.tx2 = 0
        self.ty2 = 0
        
    def custom(self, x1, y1, w1, h1, col1 = '#C62002', col2 = '#0BA00C'):
        self.x = x1
        self.y = y1
        self.w = w1
        self.h = h1
        self.color1 = col1
        self.color2 = col2
    
        
        self.tx1 = self.x - self.w / 2
        self.ty1 = self.y - self.h / 2
        self.tx2 = self.x + self.w / 2
        self.ty2 = self.y + self.h / 2    
    def show(self, tx, ty):
        if tx >= self.tx1 and ty >= self.ty1 and tx <= self.tx2 and ty <= self.ty2:
            fill(self.color2)
        else:
            fill(self.color1)
        rect(self.x, self.y, self.w, self.h)
            
    def pressed(self, tx, ty, button = 'any'):
        if button != 'any':
            if tx >= self.tx1 and ty >= self.ty1 and tx <= self.tx2 and ty <= self.ty2 and mouseButton == button:
                return True
            else:
                return False
        else:
            if tx >= self.tx1 and ty >= self.ty1 and tx <= self.tx2 and ty <= self.ty2 and mousePressed:
                return True
            else:
                return False
