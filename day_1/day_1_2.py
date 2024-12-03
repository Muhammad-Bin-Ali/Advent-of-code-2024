from collections import Counter

group1 = []
group2 = []
total_dist = 0

with open('day_1/day_1.in', 'r') as f:
    data = f.readlines()
    for line in data:
        data = f.readlines()
        loc_ids = [int(i) for i in line.split()]
        group1.append(loc_ids[0])
        group2.append(loc_ids[1])

freq_map = Counter(group2)       
        
for i in range(len(group1)):
    total_dist += abs(group1[i] * freq_map.get(group1[i], 0))
    
print(total_dist)
    