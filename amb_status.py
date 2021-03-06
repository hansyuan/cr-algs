from IPython import embed

class amb_status:
    next_id = 0

    def __init__(self):
        self.id = amb_status.next_id
        amb_status.next_id += 1

        self.deployed = False
        self.lat = -1
        self.lon = -1
        self.time_deployed = -1


    def deploy(self, time, lat, lon):
        """ Given time in seconds and physical location, 'deploy' the ambulance """ 
        self.deployed = True
        self.time_deployed = time
        self.lat = lat
        self.lon = lon

    def finish(self):
        """ Reset all internal values back to idle defaults """
        self.deployed = False
        self.time_deployed = self.lat = self.lon = -1


def main():
    """ Sanity check the class implementation. Not likely to be thorough. """
    ambulances = []
    for x in range(100):
        ambulances.append(amb_status())


    
    
    for a in ambulances:
        a.deploy(999, 999.999, 999.999)

    for a in ambulances:
        if not a.deployed:
            raise Exception("Deployment execution failed.")

    for b in ambulances:
        b.finish()

    for b in ambulances: 
        if b.deployed:
            raise Exception("Deployment return failed.")

    print("Finish tester")

if __name__ == "__main__": main()
