from __future__ import division, print_function
import time, math

def turn_90_left(lbot, verbose=False):
	lbot.rot= -math.pi/2
	lbot.setRobotSpeed(lbot.adv, lbot.rot)
	if verbose:
		print('~ Learnbot turning left ...')
	time.sleep(1)
	lbot.rot= 0