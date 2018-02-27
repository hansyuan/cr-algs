
def clockloop(data, ambs, speed):
    """ 
    NOT USING. 
    
    Run on a clock the simulation. When I run the simulator, the program
    itself should be understood to be running at a faster speed than real time. 
    """

    now = time() 

    # The original starting time of the clock is called now

    # All events that occurred from the data will be an offset from the 
    # original starting event. The first case's call time shall be the 
    # starting time stored in now (approximately.)

    for call_event in data:

        # Do the thing, then sleep.
        amb_id = pick_ambulance()
        change_states(amb_status, amb_id)
        print("The event is located at %f, %f" %(call_event.lat, call_event.lon))

        sleep_time = call_event.waittime / speed
        print("Sleep for %.2f simulator seconds or %1.2f real seconds" 
            %(call_event.waittime, sleep_time))
        
        old = time()
        sleep(sleep_time) # in units of seconds
        new = time()
        
        print("%5f real seconds has passed \n" %(new - old))

    # Loop one time per simulator second