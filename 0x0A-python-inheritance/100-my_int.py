#!/usr/bin/python3
"""my integer"""


class MyInt(int):
    """inherite from int"""

    def __eq__(self, obj):
        return super().__ne__(obj)

    def __ne__(self, obj):
        return super().__eq__(obj)
