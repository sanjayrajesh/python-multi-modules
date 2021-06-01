#!/usr/bin/env python

try:
    from app1.module2 import script1
except ModuleNotFoundError:
    import script1
except ImportError:
    from src.app1.module2 import script1
import os


class Class_Script:
    @staticmethod
    def Get_Script_Name():
        return os.path.basename(__file__)

    @staticmethod
    def Say_Hi():
        try:
            message = f'Hi from {Class_Script.Say_Hi.__name__} from {Class_Script.__name__}'
        except Exception:
            return None
        else:
            return message


def Main():
    print(
        f'This is the {Main.__name__}() function from {Class_Script.Get_Script_Name()}')
    print(f'This is called from -> {script1.Class_Script.Get_Script_Name()}')
    print(f'{script1.Class_Script.Say_Hi()} | This is called from -> {script1.Class_Script.Get_Script_Name()}')


if __name__ == '__main__':
    Main()