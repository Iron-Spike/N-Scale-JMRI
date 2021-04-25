# This WAS an example script for a JMRI "Automat" in Python
# It is based on the AutomatonExample.
#
# It listens to two sensors, running a locomotive back and
# forth between them by changing its direction when a sensor
# detects the engine.
#
# Author:  Howard Watkins, January 2007.
# Part of the JMRI distribution

import jarray
import jmri

class Test14(jmri.jmrit.automat.AbstractAutomaton) :

    def init(self):
        # init() is called exactly once at the beginning to do
        # any necessary configuration.
        print "Inside init(self)"

        # set up sensor numbers
        # fwdSensor is reached when loco is running forward
        self.fwdSensor = sensors.provideSensor("AR24")
	self.fwdBlock = sensors.provideSensor("AR5")
        self.revSensor = sensors.provideSensor("AR22")
	self.revBlock = sensors.provideSensor("AR4")

        # get loco address. For long address change "False" to "True"
        self.throttle = self.getThrottle(5203, True)  # long address 5203

        return

    def handle(self):
        # handle() is called repeatedly until it returns false.
        print "Inside handle(self)"

	# print "initialize turnout"
    	turnouts.provideTurnout("LT1").setState(CLOSED)
    	self.waitMsec(500)         # time is in milliseconds

        # turn on whistle, 
        self.throttle.setF2(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle.setF2(False)    # turn off whistle
        self.waitMsec(3000)           # wait for 3 second        
	
	# turn on whistle, 
        self.throttle.setF2(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle.setF2(False)    # turn off whistle
        self.waitMsec(3000)           # wait for 3 second    

        # set loco to forward
        print "Set Loco Forward"
        self.throttle.setIsForward(True)

        # wait 2 second for layout to catch up, then set speed
        self.waitMsec(2000)

	print "Set speed to 1"
	self.throttle.setSpeedSetting(0.01)
	self.waitMsec(2500)
	print "Set speed to 2"
	self.throttle.setSpeedSetting(0.02)
	self.waitMsec(2000)
	print "Set speed to 3"
	self.throttle.setSpeedSetting(0.03)
	self.waitMsec(1500)
	print "Set speed to 4"
	self.throttle.setSpeedSetting(0.04)
	self.waitMsec(1000)
	print "Set speed to 5"
	self.throttle.setSpeedSetting(0.05)
	self.waitMsec(1000)
	print "Set speed to 6"
	self.throttle.setSpeedSetting(0.06)
	self.waitMsec(750)
	print "Set speed to 7"
	self.throttle.setSpeedSetting(0.07)
	self.waitMsec(500)	
	print "Set speed to 8"
	self.throttle.setSpeedSetting(0.08)
	self.waitMsec(500)
	print "Set speed to 9"
	self.throttle.setSpeedSetting(0.09)

        # wait for block sensor in forward direction to trigger, then slow
        print "Wait for Forward block Sensor"
        self.waitSensorActive(self.fwdBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.05)

        # wait for sensor in forward direction to trigger, then stop
        print "Wait for Forward Sensor"
        self.waitSensorActive(self.fwdSensor)
        print "Set speed to 2"
	self.throttle.setSpeedSetting(0.02)
	# self.waitMsec(500)
	print "Set Speed Stop"
        self.throttle.setSpeedSetting(0)

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "waiting 10 seconds"
        self.waitMsec(10000)          # wait for 10 seconds

        # turn on whistle, set direction to reverse, set speed
        self.throttle.setF2(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle.setF2(False)    # turn off whistle
        self.waitMsec(3000)           # wait for 1 second
        self.throttle.setF2(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle.setF2(False)    # turn off whistle
        self.waitMsec(3000)           # wait for 1 second

        # print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(5000)                 # wait 5 second for Xpressnet to catch up

	print "Set speed to 1"
	self.throttle.setSpeedSetting(0.01)
	self.waitMsec(2500)
	print "Set speed to 2"
	self.throttle.setSpeedSetting(0.02)
	self.waitMsec(2000)
	print "Set speed to 3"
	self.throttle.setSpeedSetting(0.03)
	self.waitMsec(1500)
	print "Set speed to 4"
	self.throttle.setSpeedSetting(0.04)
	self.waitMsec(1000)
	print "Set speed to 5"
	self.throttle.setSpeedSetting(0.05)
	self.waitMsec(1000)
	print "Set speed to 6"
	self.throttle.setSpeedSetting(0.06)
	self.waitMsec(750)
	print "Set speed to 7"
	self.throttle.setSpeedSetting(0.07)
	self.waitMsec(500)	
	print "Set speed to 8"
	self.throttle.setSpeedSetting(0.08)
	self.waitMsec(500)
	print "Set speed to 9"
	self.throttle.setSpeedSetting(0.09)

        # wait for block sensor in reverse direction to trigger, then slow
        print "Wait for reverse block Sensor"
        self.waitSensorActive(self.revBlock)
	print "Set speed to 1"
	self.throttle.setSpeedSetting(0.01)
	self.waitMsec(500)
	print "Set Slowing speed to 2"
	self.throttle.setSpeedSetting(0.02)
	self.waitMsec(500)
	print "Set Slowing speed to 3"
	self.throttle.setSpeedSetting(0.03)
	self.waitMsec(500)
	print "Set Slowing speed to 4"
	self.throttle.setSpeedSetting(0.04)
	self.waitMsec(500)
	print "Set Slowing speed to 5"
	self.throttle.setSpeedSetting(0.05)
	self.waitMsec(500)
	print "Set Slowing speed to 6"
	self.throttle.setSpeedSetting(0.06)
	self.waitMsec(500)
	print "Set Slowing speed to 7"
	self.throttle.setSpeedSetting(0.07)
	self.waitMsec(500)	
	print "Set Slowing speed to 8"
	self.throttle.setSpeedSetting(0.08)
	self.waitMsec(500)
	print "Set Slowing speed to 9"
	self.throttle.setSpeedSetting(0.09)
	self.waitMsec(500)

        # wait for sensor in reverse direction to trigger
        print "Wait for Reverse Sensor"
        self.waitSensorActive(self.revSensor)
        print "Set Speed Stop, Car de-coupled"
        self.throttle.setSpeedSetting(0)
        # set loco to forward
        print "Set Loco Forward"
        self.throttle.setIsForward(True)
	self.throttle.setSpeedSetting(0.05)
	#self.waitMsec(200)
        self.throttle.setSpeedSetting(0)
        # print "Set Loco Reverse"
        self.throttle.setIsForward(False)
	self.throttle.setSpeedSetting(0.05)
	self.waitMsec(1000)
        self.throttle.setSpeedSetting(0)

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 3 seconds"
        self.waitMsec(3000)          # wait for 3 seconds

        # turn on whistle, set direction to forward, set speed
        self.throttle.setF2(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle.setF2(False)    # turn off whistle
        self.waitMsec(1000)           # wait for 1 second


        # set loco to forward
        print "Set Loco Forward"
        self.throttle.setIsForward(True)

        # wait 1 second for layout to catch up, then set speed
        self.waitMsec(1000)
        print "Set Speed"
        self.throttle.setSpeedSetting(0.3)

        # wait for block sensor in forward direction to trigger, then slow
        print "Wait for Forward block Sensor"
        self.waitSensorActive(self.fwdBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

        # wait for sensor in forward direction to trigger, then stop
        print "Wait for Forward Sensor"
        self.waitSensorActive(self.fwdSensor)
        print "Set Speed Stop"
        self.throttle.setSpeedSetting(0)

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "waiting 10 seconds"
        self.waitMsec(10000)          # wait for 5 seconds

        # turn on whistle, set direction to reverse, set speed
        self.throttle.setF2(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle.setF2(False)    # turn off whistle
        self.waitMsec(1000)           # wait for 1 second

        # print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(1000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.2)

        # wait for block sensor in reverse direction to trigger, then slow
        print "Wait for reverse block Sensor"
        self.waitSensorActive(self.revBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

        # wait for sensor in reverse direction to trigger
        print "Wait for Reverse Sensor"
        self.waitSensorActive(self.revSensor)

	# couple car
	print "begin re-coupling car"
	print "Set Slowing speed to 9"
	self.throttle.setSpeedSetting(0.09)
	self.waitMsec(500)
	print "Set to 0.8"
	self.throttle.setSpeedSetting(0.08)
	self.waitMsec(500)
	print "Set to 0.7"
	self.throttle.setSpeedSetting(0.07)
	# self.waitMsec(500)
	print "Set to 0.6"
	self.throttle.setSpeedSetting(0.06)
	# self.waitMsec(500)
	print "Set to 0.5"
	self.throttle.setSpeedSetting(0.05)
	print "Set to 0.4"
	self.throttle.setSpeedSetting(0.04)
	print "Set to 0.3"
	self.throttle.setSpeedSetting(0.03)
	print "Set to 0.2"
	self.throttle.setSpeedSetting(0.02)
	print "Set to 0.1"
	self.throttle.setSpeedSetting(0.01)
	print "Set to 0"
	self.throttle.setSpeedSetting(0.00)

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 5 seconds"
        self.waitMsec(5000)          # wait for 5 seconds

        # and continue around again
        print "End of Loop"
        return 1
        # (requires JMRI to be terminated to stop - caution
        # doing so could leave loco running if not careful)

# end of class definition

# start one of these up
Test14().start()
