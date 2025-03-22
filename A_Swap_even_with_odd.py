t = int(input().strip())  
results = []
 
for _ in range(t):
    s = input().strip() 
    digits = list(map(int, s))
    odd = [d for d in digits if d % 2 != 0]
    even = [d for d in digits if d % 2 == 0]
    ans = []
    odd_index=-0
    even_index = 0
    odd_len= len(odd)
    even_len = len(even)
 
    while odd_index < odd_len and even_index < even_len:
        if odd[odd_index] < even[even_index]:
            ans.append(str(odd[odd_index]))
            odd_index += 1
        else:
            ans.append(str(even[even_index]))
            even_index += 1
 
    while odd_index < odd_len:
        ans.append(str(odd[odd_index]))
        odd_index += 1
 
    while even_index < even_len:
        ans.append(str(even[even_index]))
        even_index += 1
 
    results.append(''.join(ans))
 
for result in results:
    print(result)