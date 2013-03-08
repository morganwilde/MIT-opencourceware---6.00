# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb   = maxBirthProb
        self.clearProb      = clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns False.
        """
        if random.random() <= self.clearProb:
            return True
        else:
            return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        probabilityReproduction = self.maxBirthProb * (1 - popDensity)
        if random.random() <= probabilityReproduction:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException



class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        # Find clearing viruses
        newViruses = []
        for virus in self.viruses:
            if virus.doesClear():
                pass
            else:
                newViruses.append(virus)

        # Find reproducing viruses
        newPopDensity = len(newViruses)
        tempViruses = newViruses[:]
        for virus in newViruses:
            try:
                reproductionResult = virus.reproduce(newPopDensity/self.maxPop)
            except:
                pass
            else:
                tempViruses.append(reproductionResult)

        # Update patient
        self.viruses = tempViruses
        return len(self.viruses)

#
# PROBLEM 2
#
def simulationWithoutDrug(plot = True):
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    # instanciate viruses
    viruses = []
    for i in range(100):
        viruses.append( SimpleVirus(0.1, 0.05) )

    # intstanciate patient
    patient = SimplePatient(viruses, 1000)

    # run simulation
    xAxis = range(1, 301)
    yAxis = []
    yMax = 0
    growthStops = 0
    for i in range(300):
        updated = patient.update()
        if updated > yMax:
            yMax = updated
        if len(yAxis) > 40:
            if yAxis[-1] > updated and\
               yAxis[-1] > yAxis[-40] and\
               growthStops == 0:
                growthStops = i-1
        yAxis.append(updated)

    if plot == True:
        # plot it
        pylab.plot(xAxis, yAxis)
        pylab.title('Simulating virus growth in a patient over time')
        pylab.xlabel('Time steps')
        pylab.ylabel('Virus population')
        pylab.annotate('Growth stops (step no = '+str(growthStops)+')',\
                       xy=(growthStops, yAxis[growthStops]),\
                       xytext=(growthStops+15, yAxis[growthStops]-175),\
                       arrowprops=dict(facecolor='black', shrink=0.05))
        pylab.ion()
        pylab.show()
    elif plot == 'peak':
        return growthStops
    else:
        return yAxis

def runSimulations(times = 1):
    """
    runs the simulationWithoutDrug() simulation times number of times
    """
    simulationResults = []
    fileData = open('plot-data-'+str(times)+'.txt', 'a')
    for time in range(times):
        simulationResults.append( simulationWithoutDrug(False)[-1] )
        fileData.write(str(simulationWithoutDrug(False)[-1]) + '\n')

    # plot it
    pylab.plot(simulationResults, 'bo')
    pylab.title('Final population after simulation')
    pylab.xlabel('Simulation number')
    pylab.ylabel('Final virus population')
    pylab.ion()
    pylab.show()

def runSimulationsPeak(times = 1):
    """
    runs times times to average the peak
    """
    simulationResults = []
    fileData = open('plot-data-peaks-'+str(times)+'.txt', 'a')
    for time in range(times):
        simulationResults.append( simulationWithoutDrug('peak') )
        fileData.write(str(simulationWithoutDrug('peak')) + '\n')

    # plot it
    print simulationResults
    pylab.plot(simulationResults, 'bo')
    pylab.title('How long does it take before population stops growing?')
    pylab.xlabel('Simulation number')
    pylab.ylabel('Steps before growth stopped')
    pylab.ion()
    pylab.show()

#
# Test harness
#
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

if __name__ == '__main__':
    simulationWithoutDrug()
    # Collect sample
    #runSimulations(1)
    #runSimulations(10)
    #runSimulations(100)
    #runSimulations(1000)
    # Collect peak samples
##    runSimulationsPeak(1)
##    runSimulationsPeak(10)
##    runSimulationsPeak(100)
##    runSimulationsPeak(1000)

    # Find min/max for samples
##    samples = [1, 10, 100, 1000]
##    minmaxDict = {}
##    for sample in samples:
##        minmaxDict[str(sample)+'-min'] = 0
##        minmaxDict[str(sample)+'-max'] = 0
##        minmaxDict[str(sample)+'-mean'] = 0
##        minmaxDict[str(sample)+'-list'] = []
##        sums = 0
##        fileData = open('plot-data-'+str(sample)+'.txt', 'r')
##        for line in fileData:
##            result = int(line)
##            minmaxDict[str(sample)+'-list'].append(result)
##            sums += result
##            if result < minmaxDict[str(sample)+'-min'] or minmaxDict[str(sample)+'-min'] == 0:
##                minmaxDict[str(sample)+'-min'] = result
##            if result > minmaxDict[str(sample)+'-max']:
##                minmaxDict[str(sample)+'-max'] = result
##        # find mean
##        minmaxDict[str(sample)+'-mean'] = sums/sample

    # Find growth stop from samples
##    samples = [1, 10, 100, 1000]
##    minmaxDict = {}
##    for sample in samples:
##        minmaxDict[str(sample)+'-mean'] = 0
##        minmaxDict[str(sample)+'-list'] = []
##        sums = 0
##        fileData = open('plot-data-peaks-'+str(sample)+'.txt', 'r')
##        for line in fileData:
##            result = int(line)
##            minmaxDict[str(sample)+'-list'].append(result)
##            sums += result
##        # find mean
##        minmaxDict[str(sample)+'-mean'] = sums/sample
##    print '1000 mean:', minmaxDict['1000-mean']
##    print 'standard deviation of 1000:', stdDev(minmaxDict['1000-list'])

    # Print results
##    print '1 min:', minmaxDict['1-min']
##    print '1 max:', minmaxDict['1-max']
##    print '1 mean:', minmaxDict['1-mean']
##    print '10 min:', minmaxDict['10-min']
##    print '10 max:', minmaxDict['10-max']
##    print '10 mean:', minmaxDict['10-mean']
##    print 'standard deviation of 10:', stdDev(minmaxDict['10-list'])
##    print '100 min:', minmaxDict['100-min']
##    print '100 max:', minmaxDict['100-max']
##    print '100 mean:', minmaxDict['100-mean']
##    print 'standard deviation of 100:', stdDev(minmaxDict['100-list'])
##    print '1000 min:', minmaxDict['1000-min']
##    print '1000 max:', minmaxDict['1000-max']
##    print '1000 mean:', minmaxDict['1000-mean']
##    print 'standard deviation of 1000:', stdDev(minmaxDict['1000-list'])

    # Plot results
##    pylab.hist(minmaxDict['1000-list'], bins = 20)
##    pylab.hist(minmaxDict['100-list'], bins = 20)
##    pylab.hist(minmaxDict['10-list'], bins = 20)
##    pylab.title('Final virus populations after 10, 100, 100 simulations')
##    pylab.xlabel('Numer of viruses at the end')
##    pylab.ylabel('How many times it appears')
##    pylab.ion()
##    pylab.show()
    pass
