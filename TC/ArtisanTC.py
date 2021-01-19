#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:24:04 2020

@author: pi
"""

import time
#import matplotlib.pyplot as plt
from max31855 import MAX31855, MAX31855Error

cs_pin = [8]
clock_pin = 11
data_pin = 9
units = "c"
running = True


thermocouple = MAX31855(cs, clock_pin, data_pin, units)
print(thermocouple.get())
#            print("TC = {}, RJ = {}".format(thermocouple.get(), thermocouple.get_rj()))
thermocouple.cleanup()