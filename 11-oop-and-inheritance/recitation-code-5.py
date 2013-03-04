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

def get_age(person):
    return person['age']

def set_age(person, age):
    person['age'] = age

def get_height(person):
    return person['height']

def set_height(person, height):
    person['height'] = height

def get_weight(person):
    return person['weight']

def set_weight(person, weight):
    person['weight'] = weight

def print_person(person):
    print 'Name:', get_name(person), ', Age:', get_age(person)

mitch = make_person('Mitch', 32, 70, 200)
sarina = make_person('Sarina', 25, 65, 130)

print_person(mitch)
set_age(mitch, 25)
print_person(mitch)
