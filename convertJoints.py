import json
from os import listdir
from pprint import pprint


def readJointsPos(directory):
	jointPos = {"rightShoulder":[],"leftShoulder":[],"leftElbow":[],"rightElbow":[],"leftWrist":[],"rightWrist":[]}
	for fileName in listdir(directory):
		data = json.load(open(directory+'/'+fileName))
	
		jointPos['rightShoulder'].append(data["part_candidates"][0]["2"])
		jointPos['leftShoulder'].append(data["part_candidates"][0]["5"])

		jointPos['leftElbow'].append(data["part_candidates"][0]["3"])
		jointPos['rightElbow'].append(data["part_candidates"][0]["6"])

		jointPos['leftWrist'].append(data["part_candidates"][0]["4"])
		jointPos['rightWrist'].append(data["part_candidates"][0]["7"])
		
	return jointPos

def convertElbowPos():
	pass

def convertWristPos():
	pass

def convertShoulderPos():
	pass






if __name__ == "__main__":
	jointsPos = readJointsPos("json")
