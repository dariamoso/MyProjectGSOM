#Python Task 2
def is_power(num, poww):
    helper = 1
    while helper < num:
        helper*= poww
    return helper==num

print(is_power(16, 2))
print(is_power(12, 2))
print(is_power(1, 1))