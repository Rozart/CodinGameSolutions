n = int(input())
results = {}
for i in range(n):
    input_time = input()
    time = input_time.split(':')
    results[int(time[0]) * 3600 + int(time[1])
            * 60 + int(time[2])] = input_time

print(results[min(results.keys())])
