from __future__ import print_function, absolute_import

def is_there_ground(lbot):
	gsensors = lbot.getGroundSensors()
	return gsensors["left"]>50 and gsensors["right"]>50
