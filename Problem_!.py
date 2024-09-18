def min_crossing_time(times, total_time, people_left, on_other_side, current_time, path):
    if len(people_left) == 0:
        return current_time, path

    min_time = 1000
    best_path = []

    for i in range(len(people_left)):
        for j in range(i + 1, len(people_left)):
            person1 = people_left[i]
            person2 = people_left[j]
            print("till now persons are",person1,person2)
            crossing_time = max(times[person1], times[person2])
            new_time = current_time + crossing_time


            if new_time > total_time:
                continue

            new_people_left = people_left[:]
            del new_people_left[j]
            del new_people_left[i]

            new_other_side = on_other_side + [person1, person2]

            if len(new_people_left) == 0:
                return new_time, path + [(person1, person2)]

            returning_person = new_other_side[0]
            for person in new_other_side:
                if times[person] < times[returning_person]:
                    returning_person = person

            return_time = new_time + times[returning_person]

            if return_time > total_time:
                continue

            updated_people_left = new_people_left + [returning_person]
            updated_other_side = []
            for p in new_other_side:
                if p != returning_person:
                    updated_other_side.append(p)

            next_time, next_path = min_crossing_time(times, total_time, updated_people_left, updated_other_side,
                                                     return_time, path + [(person1, person2), (returning_person,)])

            if next_time < min_time:
                min_time = next_time
                best_path = next_path

    return min_time, best_path
def print_crossing_steps(result, times):
    if isinstance(result, tuple):
        min_time, path = result
        print(f"Minimum time taken: {min_time} seconds")
        print("Steps for crossing:")

        for step in path:
            if len(step) == 2:
                print(f"Crossed: {times[step[0]]} and {times[step[1]]}")
            elif len(step) == 1:
                print(f"Returned: {times[step[0]]}")
    else:
        print(result)
def river_crossing(times, total_time):
    people = list(range(len(times)))

    min_time, path = min_crossing_time(times, total_time, people, [], 0, [])

    if min_time <= total_time:
        return min_time, path
    else:
        return "It is impossible to cross within the given time."


times = [8,12,6,1,3]
total_time = 30
result = river_crossing(times, total_time)

print_crossing_steps(result, times)




