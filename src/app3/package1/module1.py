import inspect
import sys
import os


class Export_Object:
    """A class which offers a set of implementations that extract information from objects, such as classes, functions, methods, attributes and many more.
    By default, all the information will be stored into an output file.
    """

    object_info_file = 'object_info.md'

    @staticmethod
    def Import_Object(x_obj):
        print(f'Object has been imported -> {x_obj}')

    @staticmethod
    def Get_Classes(obj):
        members = inspect.getmembers(obj, inspect.isclass)
        print(members)