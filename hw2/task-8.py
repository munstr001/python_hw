class SpaceShip:
    def __init__(self, name, fuel):
        if fuel < 0:
            raise ValueError('Топливо не может быть отрицательным')
        self.name = name
        self.fuel = fuel
        self.hull = 100
        self.speed = 0
        self.crew = []

    def add_crew(self, member):
        self.crew.append(member)

    def refuel(self, amount):
        if amount <= 0:
            raise ValueError('Количество топлива должно быть положительным')
        self.fuel += amount

    def accelerate(self, amount):
        if amount <= 0:
            raise ValueError('Ускорение должно быть положительным')
        if self.hull == 0:
            raise ValueError('Корабль разрушен')
        if not any(member.role == 'пилот' and member.health > 0 for member in self.crew):
            raise ValueError('Нет здорового пилота')
        cost = amount * 0.5
        if cost > self.fuel:
            raise ValueError('Не хватает топлива')
        self.fuel -= cost
        self.speed += amount

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError('Урон не может быть отрицательным')
        self.hull = max(0, self.hull - amount)
        if self.hull == 0:
            self.speed = 0

    def status(self):
        return f'{self.name}: топливо {self.fuel}, корпус {self.hull}%, скорость {self.speed}'


class CrewMember:
    def __init__(self, name, role, skills):
        self.name = name
        self.role = role
        self.skills = skills
        self.health = 100

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError('Урон не может быть отрицательным')
        self.health = max(0, self.health - amount)

    def heal(self, amount):
        if amount <= 0:
            raise ValueError('Лечение должно быть положительным')
        self.health = min(100, self.health + amount)

    def repair(self, ship, resources):
        if self.role != 'инженер' or self.health == 0 or 'ремонт' not in self.skills:
            raise ValueError('Этот член экипажа не может ремонтировать корабль')
        if ship.hull == 0:
            raise ValueError('Разрушенный корабль не восстановить')
        if resources.get('запчасти', 0) < 1:
            raise ValueError('Нет запчастей')
        if ship.hull < 100:
            resources['запчасти'] -= 1
            ship.hull = min(100, ship.hull + 20)


class Mission:
    def __init__(self, name, goals, resources):
        self.name = name
        self.goals = list(goals)
        self.resources = dict(resources)
        self.completed_goals = []
        self.events = ['авария', 'астероиды', 'тихий полет']

    def handle_event(self, ship, event):
        if event not in self.events:
            raise ValueError('Неизвестное событие')
        print('Событие:', event)
        if event == 'авария':
            ship.take_damage(20)
            for member in ship.crew:
                member.take_damage(10)
        elif event == 'астероиды':
            pilot = any(member.role == 'пилот' and member.health > 0
                        and 'маневрирование' in member.skills for member in ship.crew)
            ship.take_damage(10 if pilot else 30)

    def complete_goal(self, goal, ship):
        if goal not in self.goals:
            raise ValueError('Такой цели нет')
        if goal in self.completed_goals:
            return
        if ship.hull == 0 or not any(member.health > 0 for member in ship.crew):
            raise ValueError('Продолжение миссии невозможно')
        if self.resources.get('припасы', 0) < 1:
            raise ValueError('Закончились припасы')
        self.resources['припасы'] -= 1
        self.completed_goals.append(goal)

    def is_completed(self):
        return all(goal in self.completed_goals for goal in self.goals)


if __name__ == '__main__':
    ship = SpaceShip('Восток', 100)
    pilot = CrewMember('Иван', 'пилот', ['маневрирование'])
    engineer = CrewMember('Анна', 'инженер', ['ремонт'])
    ship.add_crew(pilot)
    ship.add_crew(engineer)
    mission = Mission('Разведка', ['Долететь до планеты', 'Собрать образцы'],
                      {'припасы': 5, 'запчасти': 2})
    ship.accelerate(50)
    mission.handle_event(ship, 'астероиды')
    mission.complete_goal('Долететь до планеты', ship)
    mission.handle_event(ship, 'авария')
    engineer.repair(ship, mission.resources)
    pilot.heal(10)
    mission.complete_goal('Собрать образцы', ship)
    print(ship.status())
    print('Ресурсы:', mission.resources)
    print('Миссия выполнена:', mission.is_completed())
