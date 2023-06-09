from Schedule import *

my_schedule = FullSchedule(5, 4, [
    Cargo(k=3, t=1, name="Cargo1"),
    Cargo(k=5, t=1, name="Cargo2"),
    Cargo(k=5, t=3, name="Cargo3")
])


#my_schedule = FullSchedule(6, 10, [
#    Cargo(k=3, t=1, name="Cargo1"),
#    Cargo(k=5, t=1, name="Cargo2"),
#    Cargo(k=5, t=3, name="Cargo3"),
#    Cargo(k=4, t=2, name="Cargo4"),
#    Cargo(k=6, t=4, name="Cargo5")
#])

#my_schedule = FullSchedule(10, 7, [
#    Cargo(k=3, t=1, name="Cargo1"),
#    Cargo(k=5, t=1, name="Cargo2"),
#    Cargo(k=5, t=3, name="Cargo3"),
#    Cargo(k=4, t=2, name="Cargo4"),
#    Cargo(k=6, t=4, name="Cargo5"),
#    Cargo(k=8, t=5, name="Cargo6"),
#    Cargo(k=2, t=6, name="Cargo7"),
#    Cargo(k=3, t=7, name="Cargo8"),
#    Cargo(k=7, t=8, name="Cargo9"),
#    Cargo(k=6, t=9, name="Cargo10"),
#])


print("greedy")
greedy_schedule = greedy_unloading(my_schedule)
greedy_schedule.display_schedule_table()

print('branch and bound with')
bb_pulp_scedule = branch_and_bound_unloading_pulp(my_schedule)
bb_pulp_scedule.display_schedule_table()

