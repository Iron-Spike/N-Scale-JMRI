# This WAS an example script for a JMRI "Automat" in Python
# It is based on the AutomatonExample.
#
# Originally the script listens to two sensors, running a locomotive back and
# forth between them by changing its direction when a sensor
# detects the engine.
# Modified to run alternate trains on two mainline yard loops out thru the layout and back
#
# Author:  original author Howard Watkins, January 2007.
# Modified by: Iron Spike Model Train Museum Volunteers, Tom Tate and Darrell Risley
# Part of the JMRI distribution

import jarray
import jmri

class Test14(jmri.jmrit.automat.AbstractAutomaton) :

    def init(self):
        # init() is called exactly once at the beginning to do
        # any necessary configuration.
        print "Inside init(self)"

        # set up sensor numbers
        # two Sensors used for each yard loop. one to slow the active locomotive and
        # second to stop
        self.sensor1 = sensors.provideSensor("LS5")
        self.sensor2 = sensors.provideSensor("LS7")
        self.sensor3 = sensors.provideSensor("LS6")
        self.sensor4 = sensors.provideSensor("LS8")

        # get loco address. For long address change 
        self.throttle1 = self.getThrottle(5253, True)  # long address 5253
        self.throttle2 = self.getThrottle(5258, True)  # long address 5258

        return

    def handle(self):
        # handle() is called repeatedly until it returns false.
        print "Inside handle(self)"

	# print "initialize turnout"
    	turnouts.provideTurnout("LT11").setState(THROWN)
    	self.waitMsec(500)         # time is in milliseconds
    	turnouts.provideTurnout("LT5").setState(THROWN)
    	self.waitMsec(500)         # time is in milliseconds

        # turn on whistle, 
        # self.throttle1.setF2(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle1.setF2(False)    # turn off whistle
        # self.waitMsec(3000)           # wait for 3 second        
	
	# turn on whistle, 
        # self.throttle1.setF2(True)     # turn on whistle
        # self.waitMsec(1000)           # wait for 1 seconds
        # self.throttle1.setF2(False)    # turn off whistle
        # self.waitMsec(3000)           # wait for 3 second    

    # set loco to forward
        print "Set Loco1 Forward"
        self.throttle1.setIsForward(True)

    # wait 2 second for layout to catch up, then set speed
        self.waitMsec(1000)

	print "Set speed to 1"
	self.throttle1.setSpeedSetting(0.01)
	self.waitMsec(2500)
	print "Set speed to 2"
	self.throttle1.setSpeedSetting(0.02)
	self.waitMsec(2000)
    print "Set speed to 3"
    self.throttle1.setSpeedSetting(0.03)
    self.waitMsec(1500)
    print "Set speed to 4"
    self.throttle1.setSpeedSetting(0.04)
    self.waitMsec(1000)
    print "Set speed to 5"
    self.throttle1.setSpeedSetting(0.05)
    self.waitMsec(1000)
    print "Set speed to 6"
    self.throttle1.setSpeedSetting(0.06)
    self.waitMsec(750)
    print "Set speed to 7"
    self.throttle1.setSpeedSetting(0.07)
    self.waitMsec(500)	
    print "Set speed to 8"
    self.throttle1.setSpeedSetting(0.08)
    self.waitMsec(500)
    print "Set speed to 9"
    self.throttle1.setSpeedSetting(0.09)

    # wait for block sensor in forward direction to trigger, then slow
    print "Wait for FIRST INNER LOOP block Sensor"
    self.waitSensorActive(self.sensor1)
    print "Set Speed Slow"
    self.throttle1.setSpeedSetting(0.05)

    # wait for sensor in forward direction to trigger, then stop
    print "Wait for 2ND INNER LOOP block Sensor"
    self.waitSensorActive(self.sensor2)
    print "Set speed to 2"
    self.throttle1.setSpeedSetting(0.02)

    # self.waitMsec(500)
    print "Set Speed Stop"
    self.throttle1.setSpeedSetting(0)

    # delay for a time (remember loco could still be moving
    # due to simulated or actual inertia). Time is in milliseconds
    print "waiting 10 seconds"
    self.waitMsec(10000)          # wait for 10 seconds

    # SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO SECOND LOCO

 	# print "initialize turnout"
    turnouts.provideTurnout("LT11").setState(CLOSED)
    self.waitMsec(500)         # time is in milliseconds
    turnouts.provideTurnout("LT5").setState(CLOSED)
    self.waitMsec(500)         # time is in milliseconds

    # turn on whistle, 
    # self.throttle2.setF2(True)     # turn on whistle
    # self.waitMsec(1000)           # wait for 1 seconds
    # self.throttle2.setF2(False)    # turn off whistle
    # self.waitMsec(3000)           # wait for 3 second        
	
	# turn on whistle, 
    # self.throttle2.setF2(True)     # turn on whistle
    # self.waitMsec(1000)           # wait for 1 seconds
    # self.throttle2.setF2(False)    # turn off whistle
    # self.waitMsec(3000)           # wait for 3 second    

    # set loco to forward
    print "Set Loco1 Forward"
    self.throttle2.setIsForward(True)

    # wait 2 second for layout to catch up, then set speed
    self.waitMsec(1000)

    print "Set speed to 1"
    self.throttle2.setSpeedSetting(0.01)
    self.waitMsec(2500)
    print "Set speed to 2"
    self.throttle2.setSpeedSetting(0.02)
    self.waitMsec(2000)
    print "Set speed to 3"
    self.throttle2.setSpeedSetting(0.03)
    self.waitMsec(1500)
    print "Set speed to 4"
    self.throttle2.setSpeedSetting(0.04)
    self.waitMsec(1000)
    print "Set speed to 5"
    self.throttle2.setSpeedSetting(0.05)
    self.waitMsec(1000)
    print "Set speed to 6"
    self.throttle2.setSpeedSetting(0.06)
    self.waitMsec(750)
    print "Set speed to 7"
    self.throttle2.setSpeedSetting(0.07)
    self.waitMsec(500)	
    print "Set speed to 8"
    self.throttle2.setSpeedSetting(0.08)
    self.waitMsec(500)
    print "Set speed to 9"
    self.throttle2.setSpeedSetting(0.09)

    # wait for block sensor in forward direction to trigger, then slow
    print "Wait for FIRST OUTER LOOP block Sensor"
    self.waitSensorActive(self.sensor3)
    print "Set Speed Slow"
    self.throttle2.setSpeedSetting(0.05)

    # wait for sensor in forward direction to trigger, then stop
    print "Wait for 2ND OUTER LOOP block Sensor"
    self.waitSensorActive(self.sensor4)
    print "Set speed to 2"
    self.throttle2.setSpeedSetting(0.02)
    # self.waitMsec(500)
    print "Set Speed Stop"
    self.throttle2.setSpeedSetting(0)

    # delay for a time (remember loco could still be moving
    # due to simulated or actual inertia). Time is in milliseconds
    print "waiting 10 seconds"
    self.waitMsec(10000)          # wait for 10 seconds

    # and continue around again
    print "End of Loop"
        return 1
    # (requires JMRI to be terminated to stop - caution
    # doing so could leave loco running if not careful)

# end of class definition

# start one of these up
Test14().start()
