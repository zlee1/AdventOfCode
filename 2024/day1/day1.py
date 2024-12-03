with open('day1\\data\\input.txt', 'r') as f:
    data = f.readlines()

l1 = []
l2 = []
for line in data:
    sp = line.split(' ')
    l1.append(int(sp[0]))
    l2.append(int(sp[-1]))

l1 = sorted(l1)
l2 = sorted(l2)

diff_sum = 0
for i in range(len(l1)):
    diff_sum += abs(l1[i] - l2[i])

print(diff_sum)

count_dict = {}

for i in range(len(l1)):
    ct = l2.count(l1[i])
    count_dict.update({l1[i]:ct})

mult_sum = 0
for i in l1:
    mult_sum += i*count_dict.get(i)

print(mult_sum)