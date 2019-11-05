from threading import Condition, Thread
import time


class Doer:
    def __init__(self):
        self.whos_turn = 1
        self.cond_1_2 = Condition()
        self.cond_2_3 = Condition()

    def _wait_for_turn(self, turn, condition):
        with condition:
            while self.whos_turn != turn:
                condition.wait()
            return

    def _let_go_next(self, turn, condition):
        self.whos_turn = turn
        with condition:
            condition.notify()

    def first(self, action):
        print('First')
        # Следующую строчку не убирать
        action()
        self._let_go_next(turn=2, condition=self.cond_1_2)

    def second(self, action):
        self._wait_for_turn(turn=2, condition=self.cond_1_2)
        print('Second')
        # Следующую строчку не убирать
        action()
        self._let_go_next(turn=3, condition=self.cond_2_3)
    
    def third(self, action):
        self._wait_for_turn(turn=3, condition=self.cond_2_3)
        print('Third')
        # Следующую строчку не убирать
        action()
        self.whos_turn = 1


def action():
    print('Processing')
    time.sleep(2)
    print('Done')


if __name__ == '__main__':
    pool = []
    doer = Doer()
    object_methods = [method_name for method_name in dir(doer)
                      if '_' not in method_name and callable(getattr(doer, method_name))]
    for m in object_methods[::-1]:
        thread = Thread(target=getattr(doer, m), args=(action,))
        thread.start()
        pool.append(thread)
        time.sleep(0.5)
    for t in pool:
        t.join()

