from two_smallest import find_two_smallest
import defines_lists

lists = [defines_lists.l1, defines_lists.l2, defines_lists.l3]

file = open('result.txt', 'w')

for l in lists:
    smlst_values = find_two_smallest(l)
    file.write(f"{smlst_values[0]} {smlst_values[1]}\n")

file.close()