from collections import OrderedDict, Counter

N = int(input())
ordered_items = OrderedDict()

for _ in range(N):
    data = input().split()
    item_name = data[:-1]
    net_price = data[-1]
    item = ' '.join(item_name)
    if item not in ordered_items:
        ordered_items[item] = int(net_price)
    else:
        ordered_items[item] += int(net_price)

for k in ordered_items: print(k, ordered_items[k])