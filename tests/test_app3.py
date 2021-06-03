import sys

app = 'App=3'

try:
    sys.path.insert(1, '../')
    import src.app3.package1.module1 as m1
except ModuleNotFoundError:
    sys.path.insert(1, '')
    import src.app3.package1.module1 as m1
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')


class Test_Class_1:
    @staticmethod
    def Test1():
        print(
            f'This is {Test_Class_1.Test1.__name__} from {Test_Class_1.__name__}')

    @staticmethod
    def Test2():
        print(
            f'This is {Test_Class_1.Test2.__name__} from {Test_Class_1.__name__}')

    @staticmethod
    def Test3():
        print(
            f'This is {Test_Class_1.Test3.__name__} from {Test_Class_1.__name__}')

    @staticmethod
    def Test4():
        print(
            f'This is {Test_Class_1.Test4.__name__} from {Test_Class_1.__name__}')


class Test_Class_2:
    @staticmethod
    def Test1():
        print(
            f'This is {Test_Class_2.Test1.__name__} from {Test_Class_2.__name__}')

    @staticmethod
    def Test2():
        print(
            f'This is {Test_Class_2.Test2.__name__} from {Test_Class_2.__name__}')

    @staticmethod
    def Test3():
        print(
            f'This is {Test_Class_2.Test3.__name__} from {Test_Class_2.__name__}')

    @staticmethod
    def Test4():
        print(
            f'This is {Test_Class_2.Test4.__name__} from {Test_Class_2.__name__}')


Y_1 = Test_Class_1


imp_Y_1 = m1.Export_Object.Import_Object(Y_1)