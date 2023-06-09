#!/usr/bin/python3
""" 4-hidden_discovery.py """
import hidden_4

def main():
    """ main """
    for name in dir(hidden_4):
        if name[0] != '_':
            print(name)

if __name__ == "__main__":
    main()
