from Schedule import FullSchedule
from copy import deepcopy
from pulp import *

# Метод ветвей и границ
def branch_and_bound_unloading_pulp(full_schedule: FullSchedule) -> FullSchedule:
    # Создаем копию исходного расписания
    new_schedule = deepcopy(full_schedule)
    
    # Создаем новую задачу линейного программирования
    prob = LpProblem("UnloadingProblem", LpMinimize)
    
    # Создаем переменные
    x = LpVariable.dicts("work", 
                         ((c.name, t) for c in new_schedule.cargo for t in range(c.t, new_schedule.end_time)),
                         lowBound=0, upBound=new_schedule.number_of_workers, cat='Integer')
                         
    # Добавляем ограничения по количеству рабочих в каждый момент времени
    for t in range(new_schedule.end_time):
        prob.addConstraint(lpSum([x[(c.name, t)] for c in new_schedule.cargo if t >= c.t and t < new_schedule.end_time]) <= new_schedule.number_of_workers)

    # Добавляем ограничения по обработке каждого груза
    for c in new_schedule.cargo:
        prob.addConstraint(lpSum([x[(c.name, t)] for t in range(c.t, new_schedule.end_time)]) >= c.k)

    # Нацеливаемся на минимизацию общего времени разгрузки
    prob.setObjective(lpSum([x[(c.name, t)] for c in new_schedule.cargo for t in range(c.t, new_schedule.end_time)]))

    # Решаем задачу
    prob.solve(PULP_CBC_CMD(msg=False))

    # Если найдено оптимальное решение, применяем его к расписанию
    if LpStatus[prob.status] == 'Optimal':
        for c in new_schedule.cargo:
            for t in range(c.t, new_schedule.end_time):
                if value(x[(c.name, t)]) > 0:
                    new_schedule.schedule_per_cargo[c][t] = value(x[(c.name, t)])
    else:
        print("Warning: Not all cargo could be unloaded within the given time frame.")
    
    return new_schedule