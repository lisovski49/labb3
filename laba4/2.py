class Room
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

length=float(input("Введите длину комнаты в метрах: "))
width=float(input("Введите ширину комнаты в метрах:"))
height=float(input("Введите высоту комнаты в метрах:"))

window_area = float(input("Введите общую площадь окон в комнате: "))
door_area = float(input("Введите общую площадь дверей в комнате: "))

room=Room(length,width,height)
calculator=WallpaperCalculator(room,window_area,door_area)
total_area=calculator.calculate_total_wall_area()

print("Общая площадь стены комнаты:", total_area, "квадратных метров")