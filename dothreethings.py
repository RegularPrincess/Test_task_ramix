import threading
import time


# in other branch You can find Doer implementation via condition and notify
class Doer:
    def __init__(self):
        self.whos_turn = 1

    def first(self, action):
        while self.whos_turn != 1:
            time.sleep(1)
        print('First')
        # Следующую строчку не убирать
        action()
        self.whos_turn = 2
    
    def second(self, action):
        while self.whos_turn != 2:
            time.sleep(1)
        print('Second')
        # Следующую строчку не убирать
        action()
        self.whos_turn = 3
    
    def third(self, action):
        while self.whos_turn != 3:
            time.sleep(1)
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
    for m in object_methods:
        thread = threading.Thread(target=getattr(doer, m), args=(action,))
        thread.start()
        pool.append(thread)
        time.sleep(0.5)
    for t in pool:
        t.join()

