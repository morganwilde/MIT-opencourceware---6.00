Introduction to Simulation and Random Walks
===========================================

### OOP

Last lecture we talked about a `Person` class, which was a superclass to `MITPerson`. `MITPerson` had a *class variable*. As subclasses to `MITPerson` we had `UG` and `G` that inherited everything from `MITPerson` up to `Person`.

`CourseList` class

```Python
class CourseList(object):
    def __init__(self, number):
        self.number = number
        self.students = []
    def addStudent(self, who):
        if not who.isStudent():
            raise TypeError('Not a student')
        if who in self.students:
            raise ValueError('Duplicate student')
        self.students.append(who)
    def remStudent(self, who):
        try:
            self.students.remove(who)
        except:
            print str(who) + ' not in ' + self.number
    def allStudents(self):
        for s in self.students:
            yield s
    def ugs(self):
        indx = 0
        while indx < len(self.students):
            if type(self.students[indx]) == UG:
                yield self.students[indx]
            indx += 1
```

`addStudent` adds a student, but it has defensive programming techniques deployed. It checks whether `who` is a student and whether this student is in the list already.

Later we instanciate these classes

```Python
m1 = MITPerson('Barbara Beaver')
ug1 = UG('Jane Doe')
ug2 = UG('John Doe')
g1 = G('Mitch Peabody')
g2 = G('Ryan Jackson')
g3 = G('Sarina Canelake')
SixHundred = CourseList('6.00')
SixHundred.addStudent(ug1)
SixHundred.addStudent(g1)
SixHundred.addStudent(ug2)
```

#### Creating interfaces

To retrieve and set inner instance variable always create and use an interface. This allows for the freedom of changing inner workings of a class without worrying that this will brake the code using objects of this class.

`yield` - is a generator (a bit like return). A generator is a function that remembers the point in the body where it last returned plus all the local variables.

### Analytic methods

Analytic models let you precisely predict behaviour given some initial conditions & some parameters. These are basically functions.

#### Example

1700 how would you do a model? By hand or mechanimal model.

### Simulation methods

1. Systems that are not matchematical tractable (Wheather forcasting)
2. Succesively refining series of simulations
3. Often easier to exctract useful intermediate results
4. Computers

Simulation - gives an estimate.

#### What a simulation looks like?

We want to build a model with the following property:

* Provides useful information about the behavior of the system (vs an analytic model which would exactly predict what the system would do)
* Provides an approximation to reality
* Simulation models are *descriptive*, not *prescriptive*

Given a particular scenario here is an approximation of what could happen.

#### Example

1827 Robert Brown a pollen particle flows in water at random. The theory of speculation. Stocastic thinking.

Brownian motion is an example of a **random walk**. The essential idea is - we have a system of related objects, and at each step each object will move in a random direction.

**Random walks** are really useful in biology.

A drunken student in a big field. Each step he can take in one of four directions (ESWN), how far away will he be after 1000 steps?

To guess, best is to develop a simple model. The student start at *origin*.

| Steps | Distance | Probability |
|-------|----------|-------------|
| 1     | 1        | 1           |
| 2     | 0        | 1/4         |
| 2     | root(2)  | 2/4         |
| 2     | 2        | 1/4         |
| 3     | 1        | 1/4         |
| 3     | 1        | 1/4         |
| 3     | root(5)  | 1/4         |
| 3     | 1        | 1/16        |
| 3     | root(5)  | 1/4         |
| 3     | 1/root(5) | 1/4        |

1. step 1
2. steps 1.2
3. steps 1.4

Do a little bit of a calculation to expect what could I expect.

So in this case I need to model:

* A drunk
* A field - something that maps drunks to locations
* A location

Think about what your model should return.
