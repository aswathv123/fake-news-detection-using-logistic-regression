# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 22:33:07 2023

@author: aswat
"""

def pattern(n):

    for i in range(n,1,-1):

        for j in range(1,i):
            print("*")
        print("\n")
pattern(6)