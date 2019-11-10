# -*- coding: utf-8 -*-


class MyIterator:
    def __init__(self, iter_obj, only_even=True):
        self._iter_obj = iter(iter_obj)
        self._even = only_even

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self._even:
                next(self._iter_obj)
                res = next(self._iter_obj)
                return res
            else:
                res = next(self._iter_obj)
                next(self._iter_obj)
                return res
        except StopIteration:
            print('End of custom iterator')
            raise StopIteration


if __name__ == '__main__':
    m = MyIterator([1, 2, 3, 4, 5, 6, 7, 8], True)
    for e in m:
        print(e)
