light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
current_x = initial_tx
current_y = initial_ty

while True:
    remaining_turns = int(input())
    result = ""

    if current_y < light_y:
        result += "S"
        current_y += 1
    elif current_y > light_y:
        result += "N"
        current_y -= 1

    if current_x > light_x:
        result += "W"
        current_x -= 1
    elif current_x < light_x:
        result += "E"
        current_x += 1

    print(result)
