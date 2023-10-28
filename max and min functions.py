def find_max(T):
    max_val = T[0]
    for i in T:
        if i > max_val:
            max_val = i
    return max_val

def find_min(T):
    min_val = T[0]
    for i in T:
        if i < min_val:
            min_val = i
    return min_val

def inverse(T):
    inverse = T[::-1]
    return inverse

T = []
for i in range(10):
    value = float(input("Enter a real number: "))
    T.append(value)

print("The maximum is", find_max(T))
print("The minimum is", find_min(T))
print("The inverse is", inverse(T))