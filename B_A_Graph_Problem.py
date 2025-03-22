
n = int(input().strip())
 
a = [0] * (n + 1)
pos = [0] * (n + 1)
 
input_line = input().strip()
input_values = input_line.split()
input_values = list(map(int, input_values))
for i in range(1, n + 1):
    a[i] = input_values[i - 1]
    pos[a[i]] = i

 
rounds = 1
for i in range(2, n + 1):
    if pos[i] > pos[i - 1]:
        rounds += 1       
print(rounds)