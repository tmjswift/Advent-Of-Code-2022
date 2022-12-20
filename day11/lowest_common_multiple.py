# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:09:37 2022

@author: Tom
"""

lowestCommonMultiple = 0
while True:
    lowestCommonMultiple = lowestCommonMultiple + 19
    if lowestCommonMultiple % 11 == 0 \
    and lowestCommonMultiple % 7 == 0 \
    and lowestCommonMultiple % 3 == 0 \
    and lowestCommonMultiple % 5 == 0 \
    and lowestCommonMultiple % 17 == 0 \
    and lowestCommonMultiple % 13 == 0 \
    and lowestCommonMultiple % 2 == 0:
        break
print(lowestCommonMultiple)
