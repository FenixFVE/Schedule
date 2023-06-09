from Schedule import FullSchedule
from copy import deepcopy

# Жадный алгоритм.
def greedy_unloading(full_schedule: FullSchedule) -> FullSchedule:
        # Создаем копию исходного расписания, чтобы не менять его в процессе работы функции
    new_schedule = deepcopy(full_schedule)

    # Проходим по всем грузам в порядке их прибытия
    for cargo in sorted(new_schedule.cargo, key=lambda x: x.t):
        # Считаем, сколько рабочих нужно для обработки текущего груза
        workers_needed = cargo.k
        # Запоминаем время прибытия груза
        arrival_time = cargo.t

        # Проходим по всем моментам времени, начиная от момента прибытия груза и до конца рабочего дня
        for time in range(arrival_time, new_schedule.end_time):
            # Если необходимое количество рабочих достигло нуля, значит, груз обработан, и мы можем прервать цикл
            if workers_needed <= 0:
                break

            # Считаем, сколько рабочих свободно в данный момент времени
            available_workers = new_schedule.number_of_workers - sum(new_schedule.schedule_per_cargo[c][time] for c in new_schedule.cargo)

            # Определяем, сколько рабочих мы можем назначить на груз в данный момент времени
            # Это будет минимальное значение из количества доступных рабочих и количества рабочих, которые еще нужны для обработки груза
            workers_to_assign = min(workers_needed, available_workers)

            # Назначаем рабочих на груз
            new_schedule.schedule_per_cargo[cargo][time] += workers_to_assign

            # Уменьшаем количество рабочих, которые еще нужны для обработки груза
            workers_needed -= workers_to_assign

    # Проверяем, удалось ли обработать все грузы в установленные временные рамки
    # Если нет, выводим предупреждение
    if any(cargo.k > sum(new_schedule.schedule_per_cargo[cargo]) for cargo in new_schedule.cargo):
        print("Warning: Not all cargo could be unloaded within the given time frame.")

    # Возвращаем новое расписание
    return new_schedule