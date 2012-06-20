import commands

def getData():
	"""
	uses the pmset command to find battery information
	"""
	powerInfo = commands.getoutput("pmset -g ps")
  
	ouputString = ""
	powerState = ""
	powerSource = ""
	powerState = ""
	percentage = ""
	time = ""

	if "AC Power" in powerInfo:
		powerSource = "AC"
	elif "Battery" in powerInfo:
		powerSource = "Battery"
	if "charged" in powerInfo:
		powerState = "Charged"
	else: 
		if "discharging" in powerInfo:
			powerState = "Discharging"
		else:
			powerState = "Charging"
	if powerState != "":
		percentOffset = powerInfo.find("%")
		percentage = powerInfo[percentOffset-2:percentOffset]
		if percentage[0] == " ":
			percentage = percentage[1:]
		timeOffset = powerInfo.find(":")
		if timeOffset >= 0:
			time = powerInfo[timeOffset-2:timeOffset+3]
			if time[0] == " ":
				time = time[1:] 
	if powerState != "":
		outputString = "<power state=\"" + powerState + "\""
		if powerSource != "":
			outputString = outputString + " source=\"" + powerSource + "\""
		if percentage != "": 
			outputString = outputString + " percent=\"" + percentage + "%\""
		if time != "":
			outputString = outputString + " time=\"" + time + "\""
		outputString = outputString + "/>"
	return outputString










