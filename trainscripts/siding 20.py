# This is an example script for a JMRI "Automat" in Python
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
	self.sidSensor = sensors.provideSensor("AR23")
	self.sidBlock = sensors.provideSensor("AR2")

        # get loco address. For long address change "False" to "True"
        self.throttle = self.getThrottle(20, False)  # short address 20

        return

    def handle(self):
        # handle() is called repeatedly until it returns false.
        print "Inside handle(self)"

	# BEGIN MOVE 1 BEGIN MOVE 1 BEGIN MOVE 1 BEGIN MOVE 1 BEGIN MOVE 1 BEGIN MOVE 1 BEGIN MOVE 1 BEGIN MOVE 1
	# CAR DELIVERY TO SIDING
 
	print "beginning move 1"
	print "initialize turnout"
    	turnouts.provideTurnout("LT1").setState(CLOSED)
    	self.waitMsec(500)         # time is in milliseconds

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

	print "THROW turnout"
    	turnouts.provideTurnout("LT1").setState(THROWN)
    	self.waitMsec(500)         # time is in milliseconds

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "waiting 10 seconds"
        self.waitMsec(10000)          # wait for 5 seconds

        # turn on whistle, set direction to reverse, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second

        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(5000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.3)

        # wait for SIDING block sensor in reverse direction to trigger, then slow
        print "Wait for SIDING block Sensor"
        self.waitSensorActive(self.sidBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

        # wait for sensor in reverse direction to trigger
        print "Wait for siding Sensor"
        self.waitSensorActive(self.sidSensor)
        print "Set Speed Stop, Car de-coupled"
        self.throttle.setSpeedSetting(0)

	# END OF MOVE 1 CAR DELIVERED TO SIDING

	# BEGIN MOVE 2 BEGIN MOVE 2 BEGIN MOVE 2 BEGIN MOVE 2 BEGIN MOVE 2 BEGIN MOVE 2 BEGIN MOVE 2 BEGIN MOVE 2
	# LOCOMOTIVE MOVED BACK TO ORIGINAL LOCATION ON LEFT BLOCK AND WAITS

	print "begin move 2"
        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 3 seconds"
        self.waitMsec(3000)          # wait for 3 seconds

	# turn on whistle, set direction to forward, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second

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

	print "CLOSE turnout"
    	turnouts.provideTurnout("LT1").setState(CLOSED)
    	self.waitMsec(500)         # time is in milliseconds

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "waiting 10 seconds"
        self.waitMsec(10000)          # wait for 5 seconds

        # turn on whistle, set direction to reverse, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second

        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(1000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.3)

        # wait for block sensor in reverse direction to trigger, then slow
        print "Wait for reverse block Sensor"
        self.waitSensorActive(self.revBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

        # wait for sensor in reverse direction to trigger
        print "Wait for Reverse Sensor"
        self.waitSensorActive(self.revSensor)

	# couple car
	# print "begin re-coupling car"
	# print "Set Slowing speed to 9"
	# self.throttle.setSpeedSetting(0.09)
	# self.waitMsec(500)
	# print "Set to 0.8"
	# self.throttle.setSpeedSetting(0.08)
	# self.waitMsec(500)
	# print "Set to 0.7"
	# self.throttle.setSpeedSetting(0.07)
	# self.waitMsec(500)
	# print "Set to 0.6"
	# self.throttle.setSpeedSetting(0.06)
	# self.waitMsec(500)
	# print "Set to 0.5"
	# self.throttle.setSpeedSetting(0.05)
	# print "Set to 0.4"
	# self.throttle.setSpeedSetting(0.04)
	# print "Set to 0.3"
	# self.throttle.setSpeedSetting(0.03)
	# print "Set to 0.2"
	# self.throttle.setSpeedSetting(0.02)
	# print "Set to 0.1"
	# self.throttle.setSpeedSetting(0.01)
	print "Set to 0"
	self.throttle.setSpeedSetting(0.00)

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 5 seconds"
        self.waitMsec(5000)          # wait for 5 seconds

	# END OF MOVE 2 END OF MOVE 2 END OF MOVE 2 END OF MOVE 2 END OF MOVE 2 END OF MOVE 2 END OF MOVE 2 END OF MOVE 2
	# LOCOMOTIVE RETURNED TO STARTING POINT IN LEFT BLOCK

	# BEGIN MOVE 3 BEGIN MOVE 3 BEGIN MOVE 3 BEGIN MOVE 3 BEGIN MOVE 3 BEGIN MOVE 3 BEGIN MOVE 3 BEGIN MOVE 3 BEGIN MOVE 3
	# LOCOMOTIVE RETURNS TO SIDING TO PICKUP CAR

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

	# set turnout to siding 
    	turnouts.provideTurnout("LT1").setState(THROWN)
    	self.waitMsec(500)         # time is in milliseconds

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "waiting 10 seconds"
        self.waitMsec(10000)          # wait for 5 seconds

        # turn on whistle, set direction to reverse, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second

        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(5000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.3)

        # wait for siding block sensor in reverse direction to trigger, then slow
        print "Wait for reverse siding block Sensor"
        self.waitSensorActive(self.sidBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

        # wait for siding sensor in reverse direction to trigger
        print "Wait for Siding Reverse Sensor"
        self.waitSensorActive(self.sidSensor)
        print "Set Speed Stop, Car de-coupled"
        self.throttle.setSpeedSetting(0)

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

	# END OF MOVE 3 END OF MOVE 3 END OF MOVE 3 END OF MOVE 3 END OF MOVE 3 END OF MOVE 3 END OF MOVE 3 END OF MOVE 3
	# LOCOMOTIVE RETURNED AND PICKED UP CAR

	# BEGIN MOVE 4 BEGIN MOVE 4 BEGIN MOVE 4 BEGIN MOVE 4 BEGIN MOVE 4 BEGIN MOVE 4 BEGIN MOVE 4 BEGIN MOVE 4 BEGIN MOVE 4
	# LOCOMOTIVE AND CAR RETURN TO STARTING POINT

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 3 seconds"
        self.waitMsec(3000)          # wait for 3 seconds

        # turn on whistle, set direction to forward, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second


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

	print "CLOSE turnout"
    	turnouts.provideTurnout("LT1").setState(CLOSED)
    	self.waitMsec(500)         # time is in milliseconds


        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "waiting 10 seconds"
        self.waitMsec(10000)          # wait for 5 seconds

        # turn on whistle, set direction to reverse, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second

        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(1000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.3)

        # wait for block sensor in reverse direction to trigger, then slow
        print "Wait for reverse block Sensor"
        self.waitSensorActive(self.revBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

        # wait for sensor in reverse direction to trigger
        print "Wait for Reverse Sensor"
        self.waitSensorActive(self.revSensor)

	# DEcouple car
	print "Set to 0"
	self.throttle.setSpeedSetting(0.00)

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 5 seconds"
        self.waitMsec(5000)          # wait for 5 seconds



	# END OF MOVE 4 END OF MOVE 4 END OF MOVE 4 END OF MOVE 4 END OF MOVE 4 END OF MOVE 4 END OF MOVE 4 END OF MOVE 4
	# LOCOMOTIVE AND RETURNED TO LEFT AND DECOUPLED CAR

	# BEGIN MOVE 5 BEGIN MOVE 5 BEGIN MOVE 5 BEGIN MOVE 5 BEGIN MOVE 5 BEGIN MOVE 5 BEGIN MOVE 5 BEGIN MOVE 5 BEGIN MOVE 5
	# LOCOMOTIVE RETURNS TO SIDING AND WAITS

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

	print "THROW turnout"
    	turnouts.provideTurnout("LT1").setState(THROWN)
    	self.waitMsec(500)         # time is in milliseconds

        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "waiting 10 seconds"
        self.waitMsec(10000)          # wait for 5 seconds

        # turn on whistle, set direction to reverse, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second

        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(5000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.3)

        # wait for SIDING block sensor in reverse direction to trigger, then slow
        print "Wait for SIDING block Sensor"
        self.waitSensorActive(self.sidBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

        # wait for sensor in reverse direction to trigger
        print "Wait for siding Sensor"
        self.waitSensorActive(self.sidSensor)
        print "Set Speed Stop, Car de-coupled"
        self.throttle.setSpeedSetting(0)

	# END OF MOVE 5 END OF MOVE 5 END OF MOVE 5 END OF MOVE 5 END OF MOVE 5 END OF MOVE 5 END OF MOVE 5 END OF MOVE 5
	# LOCOMOTIVE WAITS ON SIDING

	# BEGIN MOVE 6 BEGIN MOVE 6 BEGIN MOVE 6 BEGIN MOVE 6 BEGIN MOVE 6 BEGIN MOVE 6 BEGIN MOVE 6 BEGIN MOVE 6 BEGIN MOVE 6
	# LOCOMOTIVE RETURNS TO LEFT TO PICKUP CAR
 
        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "wait 3 seconds"
        self.waitMsec(3000)          # wait for 3 seconds

        # turn on whistle, set direction to forward, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second


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

	print "CLOSE turnout"
    	turnouts.provideTurnout("LT1").setState(CLOSED)
    	self.waitMsec(500)         # time is in milliseconds


        # delay for a time (remember loco could still be moving
        # due to simulated or actual inertia). Time is in milliseconds
        print "waiting 10 seconds"
        self.waitMsec(10000)          # wait for 5 seconds

        # turn on whistle, set direction to reverse, set speed
        # self.throttle.setF3(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle.setF3(False)    # turn off whistle
        # self.waitMsec(1000)           # wait for 1 second

        print "Set Loco Reverse"
        self.throttle.setIsForward(False)
        self.waitMsec(1000)                 # wait 1 second for Xpressnet to catch up
        print "Set Speed"
        self.throttle.setSpeedSetting(0.3)

        # wait for block sensor in reverse direction to trigger, then slow
        print "Wait for reverse block Sensor"
        self.waitSensorActive(self.revBlock)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

        # wait for sensor in reverse direction to trigger
        print "Wait for Reverse Sensor"
        self.waitSensorActive(self.revSensor)

	# DEcouple car
	#print "Set to 0"
	#self.throttle.setSpeedSetting(0.00)

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

	# END OF MOVE 6 END OF MOVE 6 END OF MOVE 6 END OF MOVE 6 END OF MOVE 6 END OF MOVE 6 END OF MOVE 6 END OF MOVE 6
	# LOCOMOTIVE AND CAR READY IN LEFT BLOCK FOR NEXT ITERATION

        # and continue around again
        print "End of Loop"
        return 1
        # (requires JMRI to be terminated to stop - caution
        # doing so could leave loco running if not careful)

# end of class definition

# start one of these up
Test14().start()
