import time
class Timing:
    def __init__(self, some_funct):
        self.num_runs = 10
        self.some_funct = some_funct

    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.some_funct(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        func_name = self.some_funct.__name__
        print(
            "Среднее время выполнения функции %s за %s запусков: %.5f секунд" % (
                func_name,
                self.num_runs,
                avg
            )
        )
        return self.some_funct(*args, **kwargs)


@Timing
def f(some_param):
    for j in range(1000000):
        pass


f(100000)
