l1 = [(1, "a"), (2, "b"), (3, "c")]

d1 = l1[0][0]
d2 = l1[1][0]
d3 = l1[2][0]
d1_value = l1[0][1]
d2_value = l1[1][1]
d3_value = l1[2][1]

final_dict = {f"{d1}:{d1_value}, {d2}:{d2_value}, {d3}:{d3_value}"}

print(final_dict)