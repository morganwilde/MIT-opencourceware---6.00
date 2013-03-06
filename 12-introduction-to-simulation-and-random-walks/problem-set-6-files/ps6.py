# -*- coding: utf-8 -*-
# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:

import sys
sys.dont_write_bytecode = True # stop generating *.pyc files

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return 'x:' + str(self.x) + ' y:' + str(self.y)
    def __repr__(self):
        return 'x:' + str(self.x) + ' y:' + str(self.y)
    def __eq__(self, other):
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else:
            return False

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # check if we're receiving correct input
        assert type(width) == int and width > 0 and type(height) == int and height > 0
        # set it up
        self.width = width
        self.height = height
        self.cleanTiles = []
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        if not pos in self.cleanTiles:
            self.cleanTiles.append(pos)
            return True
        else:
            return False

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        position = Position(m, n)
        print 'position in self.cleanTiles -', position in self.cleanTiles
        if position in self.cleanTiles:
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleanTiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        #return (random.randint(0, self.width-1), random.randint(0, self.height-1))
        return Position(random.randint(0, self.width-1), random.randint(0, self.height-1))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return int(pos.getX()) <= self.width-1 and int(pos.getY()) <= self.height-1


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = random.randint(0, 360-1)
        self.position = self.room.getRandomPosition()

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotAngle(self):
        return self.direction
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.room.cleanTileAtPosition(self.position)
        self.position = self.position.getNewPosition(self.direction, self.speed)

# Helper function to understand movement
def getMove(x, y, angle):
    """
    - takes a point and the angle of movement
    - returns point after a single move
    """
    hypotenuse = 1
    xMove = math.sin( math.radians(angle) )
    yMove = math.sqrt( hypotenuse**2 - xMove**2 )
    xNew = x + xMove
    if xMove > 0:
        yNew = y + yMove
    else:
        yNew = y - yMove

    return (xNew, yNew), yMove


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.room.cleanTileAtPosition(self.position)
        positionTest = self.position.getNewPosition(0, 0)
        print 'positionTest.getX(), positionTest.getY() :', positionTest.getX(), positionTest.getY()
        print 'self.room.isTileCleaned(positionTest.getX(), positionTest.getY()) -', self.room.isTileCleaned(positionTest.getX(), positionTest.getY())
        print 'self.room.isTileCleaned(positionTest.getX(), positionTest.getY()) != False -', self.room.isTileCleaned(positionTest.getX(), positionTest.getY()) != False
        while self.room.isTileCleaned(positionTest.getX(), positionTest.getY()) != False:
            positionTest = self.position.getNewPosition(self.direction, self.speed)
            print positionTest
            if self.room.isPositionInRoom(positionTest) and self.room.isTileCleaned(positionTest.getX(), positionTest.getY()) == False:
                self.position = positionTest
            else:
                self.direction = random.randint(0, 360-1)
        #self.position = positionTest
        print 'after:', self.position

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    room = RectangularRoom(width, height)
    robotClass = robot_type(room, speed)
    print room.getNumCleanedTiles()
    print room.getNumTiles()
    while room.getNumCleanedTiles() < room.getNumTiles():
        print room.getNumCleanedTiles()
        robotClass.updatePositionAndClean()


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20×20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20×20, 25×16, 40×10, 50×8, 80×5, and 100×4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    raise NotImplementedError

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    raise NotImplementedError

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    pass
    #raise NotImplementedError


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    raise NotImplementedError
