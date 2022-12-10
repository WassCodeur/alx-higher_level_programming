#!/usr/bin/python3
""" 4-hidden_discovery.py """
import hidden_4
if __name__ == "__main__":
    print("\n".join([name for name in dir(hidden_4) if name[0] != "_"]))
