class Class:
    static="ррр"
    def __init__(self,value):
        self.instance_variable=value

    def instance_metod(self):
        print("Это метод экземпляра")
        print("Значение переменной экземпляра:", self.instance_variable)

    @staticmethod
    def static_method():
        print("Это статический метод")
        print("Значение переменной", Class.static)


    @classmethod
    def class_method(cls):
        print("Это метод класса")
        print("Значение статической переменной:", cls.static)

obj=Class("fff")

obj.instance_metod()
print()

Class.static_method()
print()

Class.class_method()

