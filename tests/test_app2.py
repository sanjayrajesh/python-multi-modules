from datetime import datetime
import sys

app = 'App-2'


try:
    sys.path.insert(1, '')
    from src.app2.package2 import module1 as module1_p2
    from src.app2.package2 import module2 as module2_p2
except ModuleNotFoundError:
    sys.path.insert(1, '../')
    from src.app2.package2 import module1 as module1_p2
    from src.app2.package2 import module2 as module2_p2
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')


class Test_Package2_Module1:

    @staticmethod
    def test_main():
        ok_msg = f'Test @ {datetime.utcnow()}: ✅'
        fail_msg = f'Test @ {datetime.utcnow()}: ❌'
        try:
            x = module1_p2.Main()
        except Exception:
            print(fail_msg)
        else:
            print(ok_msg)

    @staticmethod
    def Start_Test():
        Test_Package2_Module1.test_main()


class Test_Package2_Module2:

    @staticmethod
    def test_givearray():
        try:
            x = module2_p2.Class_Script.Give_Array()
            assert x != None, 'Assertion failed'
        except AssertionError:
            print(
                f'Test: {Test_Package2_Module2.test_givearray.__name__} @ {datetime.utcnow()}: ❌')
        else:
            print(
                f'Test: {Test_Package2_Module2.test_givearray.__name__} @ {datetime.utcnow()}: ✅')


def Main():
    Test_Package2_Module2.test_givearray()


if __name__ == '__main__':
    Main()
