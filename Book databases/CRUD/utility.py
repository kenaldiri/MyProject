import random
import string

def random_string(length : int) -> str:
    result_of_random = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_of_random