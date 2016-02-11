while True:
    space_x, space_y = [int(i) for i in input().split()]
    mountain_h = []
    i = 0
    while i < 8:
        mountain_h.append(int(input()))
        i += 1

    sorted_mountain = sorted(mountain_h)
    highest_mountain = sorted_mountain[-1]
    is_highest = mountain_h[space_x] == highest_mountain

    if is_highest:
        print("FIRE")
    else:
        print("HOLD")
