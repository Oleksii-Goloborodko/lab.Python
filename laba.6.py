import time

class EvenMixin:

    def is_even(self):
        return True if self.value % 2 == 0 else False


class OddMixin:

    def is_odd(self):
        return True if self.value % 2 != 0 else False


class SquaringMixin:

    def is_pow(self):
        return pow(self.value , 2)


class Integer(OddMixin, EvenMixin, SquaringMixin):
    def timeit(method):
        def timed(*args, **kw):
            time_start = time.time()
            result = method(*args, **kw)
            time_end = time.time()
            print(method.__name__, ((time_end - time_start) * 1000), "ms")
            return result

        return timed

    @timeit
    def __init__(self, value):
        self.value = value





i = Integer(3)
print("Number is not couple  : " ,i.is_odd())
print("Number is couple  : " ,i.is_even())
print ("Is pow : ", i.is_pow())
