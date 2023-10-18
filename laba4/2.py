class Room:
    def __init__(self, length, width, height):
        self.length= length
        self.width= width
        self.height= height


    def calculator_wall_area(self):
        wall_area = self.length*self.height

        return wall_area

class WallpaperCalculator:
    def __init__(self,room,window_area,door_area):
        self.room=room
        self.window_area=window_area
        self.door_area=door_area

    def calculate_total_wall_area(self):
        wall_area=self.room.calculator_wall_area()
        total_openings_area=self.window_area+self.door_area
        total_wall_area=2*wall_area-total_openings_area
        return total_wall_area

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка: Введите положительное числовое значение.")
        except ValueError:
            print("Ошибка: Введите числовое значение.")
while True:
    length=get_float_input("Введите длину комнаты в метрах: ")
    width=get_float_input("Введите ширину комнаты в метрах:")
    height=get_float_input("Введите высоту комнаты в метрах:")

    window_area = get_float_input("Введите общую площадь окон в комнате: ")
    door_area = get_float_input("Введите общую площадь дверей в комнате: ")
    room=Room(length,width,height)
    calculator=WallpaperCalculator(room,window_area,door_area)
    total_area=calculator.calculate_total_wall_area()
    if total_area>0:
      print("Общая площадь стены комнаты:", total_area, "квадратных метров")
    else:
      print("Ошибка: Получено отрицательное значение.")
    choice = input("Хотите ли вы продолжить? (Введите 'да' или 'нет'): ")
    if choice.lower() != "да":
        break