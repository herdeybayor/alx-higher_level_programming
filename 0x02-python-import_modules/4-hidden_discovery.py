#!/usr/bin/python3
""" 4-hidden_discovery.py """
import hidden_4

def discover():
    """ discover """
    for name in dir(hidden_4):
        if name[:2] != "__":
            print(name)

if __name__ == "__main__":
    discover()
