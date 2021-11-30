# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet

colors = {'red' : '#ff0000',
          'orange' : '#ee6611',
          'blue' : '#0000ff',
          'green' : '#15e52e',
          'yellow' : '#dddd0a',
          'white' : '#ffffff',
          'gray' : '#aaaaaa',
          'cyan' : '#00ffff'}

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    parsed = line.split()
    star.R = float(parsed[1])
    star.color = colors[parsed[2]]
    star.m = float(parsed[3])
    star.x = float(parsed[4])
    star.y = float(parsed[5])
    star.Vx = float(parsed[6])
    star.Vy = float(parsed[7])

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    parsed = line.split()
    planet.R = float(parsed[1])
    planet.color = colors[parsed[2]]
    planet.m = float(parsed[3])
    planet.x = float(parsed[4])
    planet.y = float(parsed[5])
    planet.Vx = float(parsed[6])
    planet.Vy = float(parsed[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки имеют следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print("%s %d %s %f %f %f %f %f" %
                  (obj.type.capitalize(), obj.R, list(colors.keys())[list(colors.values()).index(obj.color)], obj.m, obj.x, obj.y,
                   obj.Vx, obj.Vy),
                  file=out_file)

if __name__ == "__main__":
    print("This module is not for direct call!")
