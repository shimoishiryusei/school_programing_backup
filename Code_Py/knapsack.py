from collections import namedtuple
import random
# 乱数シードは章の番号
random.seed(7)

Item = namedtuple('Item', ('name', 'weight', 'price'))
num = 20

item_list = []
max_weight = 5
max_price = 50

price_list = list(range(1, max_price+1))
random.shuffle(price_list)

for i in range(num):
    w = random.randint(1, max_weight)
    item = Item(i, w, price_list.pop())
    item_list.append(item)


class Knapsack:
    def __init__(self, size):
        self.size = size
        self.weight = 0
        self.value = 0
        self.items = []

    def append(self, item):
        if not self.has_room_for(item):
            raise ValueError('このアイテムは入れられません．重量オーバーです．')
        self.items.append(item)
        self.weight += item.weight
        self.value += item.price

    def has_room_for(self, item):
        return self.size >= self.weight + item.weight

    def __str__(self):
        val = '重さ {}kg / 価値 {}万円'.format(self.weight, self.value)
        return val


def greedy(items, size_limit):
    sorted_item_list = sorted(
        items, key=lambda x: x.price/x.weight, reverse=True)
    my_knapsack = Knapsack(size_limit)
    for v in sorted_item_list:
        try:
            my_knapsack.append(v)
        except ValueError:
            continue
    return my_knapsack


knap_g = greedy(item_list, 40)
print(knap_g)
