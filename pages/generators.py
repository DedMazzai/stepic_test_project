import random
import string


class DataGenerator:

    def random_string_digits(self, maxlen):
        self.symbols = string.ascii_letters + string.digits
        return "".join([random.choice(self.symbols) for i in range(random.randrange(10, maxlen))])

    def random_string(self, maxlen):
        self.symbols = string.ascii_lowercase
        return "".join([random.choice(self.symbols) for i in range(random.randrange(6, maxlen))])
