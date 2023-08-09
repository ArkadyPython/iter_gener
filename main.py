class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iterator = iter(self.list_of_list)
        self.count = -1
        self.result = []
        return self

    def __next__(self):
        self.count += 1
        if len(self.result) == self.count:
            self.count = 0
            self.result = None
            if self.result is None:
                self.result = next(self.iterator)
        return self.result[self.count]


def test_1():

    list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
    ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):

        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print(list(FlatIterator(list_of_lists_1)))


if __name__ == '__main__':
 test_1()