# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:52:18 2018

@author: Salomón Olivera Abud
"""

import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)
    
suma = int(lines[0]) + int(lines[1])

print(suma)
    