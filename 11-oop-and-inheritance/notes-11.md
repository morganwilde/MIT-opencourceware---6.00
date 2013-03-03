Object Oriented Programming (OOP) and Inheritance
===================

Abstract data types - `classes`.

OOP is not a new notion, it's been around 35 years and widely practiced for 15 years.

JAVA was the first popular language to support OOP. C++ is another one.

### Abstract data type

It's an idea that we can extend the language with user defined types and these types can be used as all built-in data types.

Abstract because we define an **interface** for each object. The interface explains what **methods** do, not how they do it.

The key idea here is **specification of a type/method/function** that tells us what that does.

#### Example

```Python
class intSet(object):
    #An intSet is a set of integers
    def __init__(self):
        """Create an empty set of integers"""
        self.numBuckets = 47
        self.vals = []
        for i in range(self.numBuckets):
            self.vals.append([])

    def hashE(self, e):
        #Private function, should not be used outside of class
        return abs(e)%len(self.vals)

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        for i in self.vals[self.hashE(e)]:
            if i == e: return
        self.vals[self.hashE(e)].append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals[self.hashE(e)]

    def __str__(self):
        """Returns a string representation of self"""
        elems = []
        for bucket in self.vals:
            for e in bucket: elems.append(e)
        elems.sort()
        result = ''
        for e in elems: result = result + str(e) + ','
        return '{' + result[:-1] + '}'
```

Everything with **__name__** underbars is a special Python method. In this case `__init__` introduces two new attributes.

`numBuckets` and `vals` are now attributes. `self` is used to refer to the object being created.

In the case of the method `insert(self, e)` - it has two attributes, but when calling it using the dot notation `s.insert(e)`, even though it may look like we're missing an argument, the object before the dot is actually the first argument.

`self` is always called the first implicit argument as an object.

`__str__` is another special Python method name, it is called automatically whenever we call say `print`.

#### Data hiding

It is considered a bad thing to manipulate `attributes` of objects directlly. That is because **specification** is completely separate from **implementation**. And when you're accessing `attributes` directly, you may break the program.

This concept is called - **data hiding**, I.e. no direct access. This is the most important development that makes add-on types useful. The things we're hiding are the instance variables, the vars that are assocciated with each instance of the object. Also hide class variables are assocciated with the class itself and there is only one copy.

### Person example in OOP

Before we write the code, we think about its types that would make it easy to write the program. This is abstracting the details of the code into a higher level of thinking.

#### Inheritance

Inheritance is taking already made implementations and inheriting its functionality.

```Python
import datetime

class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setBirthday(self, birthDate):
        #assumes birthDate is of type datetime.date
        #sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.birthday = birthDate
    def getAge(self):
        #assumes that self's birthday has been set
        #returns self's current age in days
        assert self.birthday != None
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        #return True if self's name is lexicographically greater
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
```

We have `getLastName()` because we don't want the user to even know we have an attribute `lastName`, because that depends on the implementation and we're considered with the specification here.

`__lt__` - less than. It's used here to order people names. When you compare two instances of this object say with `p1 < p2` it will refer to the `__lt__` method of your object to evaluate that expression.

`Person()` is a subclass of `object`.

```Python
class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def isStudent(self):
        return type(self)==UG or type(self)==G
```

By declaring `MITPerson(Person)` object we say that it **inherits** all the properties of the object `Person` and then adds two properties and overridenn two properties.

`nextIdNum` is a class variable. Its advantage is that I can assign a unique id to each instance of this object.

When you want to use a method of the superclass, not the subclass, you can use the superclass dot notation - `Person.__lt__(p1, p2)`.

When comparing two different objects instances, bare in mind that methods used will be of the first on the comparison.

```Python
class UG(MITPerson):
    def __init__(self, name):
        MITPerson.__init__(self, name)
        self.year = None
    def setYear(self, year):
        if year > 5:
            raise OverflowError('Too many')
        self.year = year
    def getYear(self):
        return self.year
```

When searching for properties such as `__str__` it searches first the inner most class, if Python doesn't find that method, it will work its way up until it finds the method.

```Python
class G(MITPerson):
    pass

g1 = G('Mitch Peabody')
print type(g1)
# <class '__main__.G'>
print type(g1) == G
# True
```

In this case `G(MITPerson)` is just an object with exactly the same properties as `MITPerson(Person)`. This is useful because it allows for type checking.
