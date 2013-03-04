Quiz 1 Answers and Object-Oriented Programming
==============================================

#### Question 3

Solve this by following the steps of each function call.

#### Question 4

Easiest way to solve it is to sort the letters of both words and see if there is a complete match.

#### Question 5

The key is to see if the specification is implemented fully.

#### Question 6

Work out what the functions do.

### Object Oriented Programming

Classes allow us to define custom `type`s. When you define a `class` you can group your methods and data together, aka *encapsulation*. Classes are a way of grouping methods and attributes.

OOP also provides **inheritance**. When an `object` inherits properties of a superclass, aka polymorphisms.

#### Example

Without creating a `class` how would you go about making a `person` functionality.

```Python
def make_person(name, age, height, weight):
    person = {}
    person['name'] = name
    person['age'] = age
    person['height'] = height
    person['weight'] = weight
    return person

def get_name(person):
    return person['name']

def set_name(person, name):
    person['name'] = name
```

`get_name` and `set_name` are know as **accessor** and **mutator** functions.

The problem sets in that you can pass on any `dict` as a person and because we are not creating a type, we cannot check if that is a `person`.

#### Dealing instead with Classes

When Python finds `__init__` it allocates a part of memory and calls it type `name-of-class`.

A `class` methods are scoped to instances of the classes object.

Double underbar methods are special Python methods, that allows for user defined `object` behave in a similar fashion to built-in `objects`.

`self` comes from here:

```Python
person = Person('mitch')
print mitch.get_age()
print Person.get_age(mitch) # this is where `self` comes from
# these two produce the same result
```

#### Inheritance


