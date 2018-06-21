import time

class Timer:
    def __init__(self):
        self.t = time.time()

    def restart(self):
        self.t = time.time()

    def elapsed(self):
        return time.time() - self.t

    def print_elapsed_time(self):
        print('{} sec'.format(self.elapsed()))
