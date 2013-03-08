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
def simulationWithoutDrug():
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
    for i in range(300):
        yAxis.append(patient.update())

    # plot it
    pylab.plot(xAxis, yAxis)
    pylab.title('Simulating virus growth in a patient over time')
    pylab.xlabel('Time steps')
    pylab.ylabel('Virus population')
    pylab.ion()
    pylab.show()

#
# Test harness
#
if __name__ == '__main__':
    simulationWithoutDrug()
