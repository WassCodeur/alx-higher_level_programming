#!/usr/bin/python3
"""lockedclass"""


class LockedClass:
    """a loked class"""
    __slots__ = "first_name"

    def __stattr__(self, name, value):
        """redefine an attr
        args: self(LokedClass)

        name(str)

        value(str)

        return None
        """
        if hasattr(self, name) or name != "first_name":
            raise AttributeError
        else:
            self.__dict__[name] = value
