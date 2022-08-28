#!/usr/bin/env python3
# instead of storing only one name at a time, it would be nice to be able
# to store more names simultaneously

def init(data):  # A function to initialize a data structure
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):  # A function to lookup from a data structure
    return data[label].get(name)


def store(data, *full_names):  # A function that stores names in your structure
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = ['first', 'middle', 'last']

        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]
