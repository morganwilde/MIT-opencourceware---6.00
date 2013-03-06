#
# Test facility for ps6.py
#

from ps6 import *

class testHarness(object):
    """
    does tests on the problem set
    """
    def __init__(self):
        try:
            self.speed =1
            self.tPosition = Position(2.1, 2.2)
            self.tRectangularRoom = RectangularRoom(5, 5)
            self.tRobot = Robot(self.tRectangularRoom, self.speed)
        except NameError:
            print 'One or more classes are not defined'
        
    # see if the import went well
    def testType(self):
        if type(self.tPosition) == Position and type(self.tRectangularRoom) == RectangularRoom and \
           type(self.tRobot) == Robot:
            print 'testType: passed.'
        else:
            print 'testType: failed'
            print 'tPosition type(' + str(type(self.tPosition)) + ')'
            print 'tRectangularRoom type(' + str(type(self.tRectangularRoom)) + ')'
            print 'tRobot type(' + str(type(self.tRobot)) + ')'

    # test Position methods and their output
    def testMethodsPosition(self):
        print 'getX:', self.tPosition.getX()
        print 'getY:', self.tPosition.getY()
        print 'getNewPosition('+str(self.tRobot.getRobotAngle())+', '+str(self.speed)+'):', \
              str(self.tPosition.getNewPosition(205, self.speed))
        print '__str__:', self.tPosition

if __name__ == '__main__':
    test = testHarness()
    test.testType()
    test.testMethodsPosition()
