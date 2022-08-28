#!/usr/bin/env python3

def init(data):  # A function to initialize a data structure
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):  # A function to lookup from a data structure
    return data[label].get(name)


def store(data, full_name):  # A function that stores a name in your structure
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
