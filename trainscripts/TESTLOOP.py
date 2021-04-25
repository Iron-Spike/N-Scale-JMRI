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
        self.fwdSensor = sensors.provideSensor("LS5")
    self.fwdBlock = sensors.provideSensor("LS7")
        # self.iLoopBlock3 = sensors.provideSensor("LS6")
	    # self.iLoopBlock4 = sensors.provideSensor("LS8")

        # get loco address. For long address change "False" to "True"
        self.throttle1 = self.getThrottle(5253, True)  # long address 5253
       
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
	        
        # sEND LOCOMOTIVE DOWN THE LINE
        print "Set speed to 2"
    	self.throttle1.setSpeedSetting(0.1)


    # wait for block sensor in forward direction to trigger, then slow
        print "Wait for FIRST INNER LOOP block Sensor"
        self.waitSensorActive(self.fwdSensor)
        print "Set Speed Slow"
        self.throttle.setSpeedSetting(0.1)

    # wait for sensor in forward direction to trigger, then stop
        print "Wait for 2ND INNER LOOP block Sensor"
        self.waitSensorActive(self.fwdBlock)
        print "Set speed to 2"
    	self.throttle1.setSpeedSetting(0)

    	# self.waitMsec(500)
    	print "Set Speed Stop"
        self.throttle1.setSpeedSetting(0)

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
