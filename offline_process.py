
import os
import pygame
from logging import getLogger
from time import time
from application import measurement

capture_refresh_time=1
circles=[(100,100,20),(150,150,20),(200,200,20),(250,250,20)]
mes = measurement.Measure('results/', circles, capture_refresh_time)
slope, concentration = mes.run()
print(slope,concentration)
