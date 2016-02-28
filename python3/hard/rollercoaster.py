number_of_places, times_per_day, number_of_groups = [
    int(i) for i in input().split()]
queue = [int(input()) for i in range(number_of_groups)]

income = 0
all_people = sum(x for x in queue)
if all_people <= number_of_places:
    income += all_people * times_per_day
else:
    incomes = [0] * number_of_groups
    group_indexes = [0] * number_of_groups

    for i in range(number_of_groups):
        current_index = i
        while True:
            next_group = queue[current_index]

            if incomes[i] + next_group > number_of_places:
                break
            incomes[i] += next_group

            current_index += 1

            if current_index == i:
                break

            if current_index >= len(queue):
                current_index = 0

        group_indexes[i] = current_index

        
    current_index = 0
    for i in range(times_per_day):
        income += incomes[current_index]
        current_index = group_indexes[current_index]

print(income)
