# -*- coding: utf-8 -*-


class MyIterator:
    def __init__(self, iter_obj, only_even=True):
        self._iter_obj = iter(iter_obj)
        self._even = only_even
        if only_even:
            self._is_to_return = False
        else:
            self._is_to_return = True

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                res = next(self._iter_obj)
                if self._is_to_return:
                    self._is_to_return = not self._is_to_return
                    return res
                self._is_to_return = not self._is_to_return
            except StopIteration:
                print('End of custom iterator')
                raise StopIteration


if __name__ == '__main__':
    m = MyIterator([1, 2, 3, 4, 5, 6, 7, 8], False)
    for e in m:
        print(e)
