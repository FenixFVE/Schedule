from dataclasses import dataclass
from typing import List, Dict
from tabulate import tabulate
from copy import deepcopy

@dataclass(eq=True, frozen=True)
class Cargo:
    k: int      # Необходимые человеко-часы на работу
    t: int      # Время прибытия груза
    name: str   # Название граза

FullCargo = List[Cargo]

WorkersPerCargo = List[int] #Количество рабочих назначенных на один груз в каждые момент времени

CargoShedule = Dict[Cargo, WorkersPerCargo] #Расписание рабочих для каждого груза

class FullSchedule:
    def __init__(self, t: int, m: int, cargo: FullCargo):
        self.cargo: FullCargo = cargo # Список грузов
        self.end_time: int = t # Время окончания работы
        self.number_of_workers: int = m # Количество рабочих
        self.schedule_per_cargo: CargoShedule = {
            cargo_item: [0] * t for cargo_item in cargo
        } # Расписание рабочих для каждого груза. Инициализируется нулевыми значениями для каждого груза и каждого временного слота.
    
    def display_schedule_table(self):
        cargo_data = [(cargo.name, cargo.k, cargo.t) for cargo in self.cargo]
        schedule_data = [
            [workers for workers in self.schedule_per_cargo[cargo]]
            for cargo in self.cargo
        ] # Данные о расписании: количество рабочих для каждого груза и каждого временного слота
        table = tabulate(
            schedule_data,
            headers=["Cargo(k,t) / t"] + list(range(self.end_time)),
            showindex=cargo_data,
            tablefmt="fancy_grid"
        ) # Форматирование таблицы расписания
        print()
        print(table)
        print() # Вывод таблицы расписания на печать

    def display_cargo_volume_table(self):
        copy = deepcopy(self)
        for cargo in copy.cargo:
            copy.schedule_per_cargo[cargo][cargo.t] = cargo.k
        copy.display_schedule_table()
