import random
import string

symbols_list = [random.choice(string.ascii_uppercase) for i in range(3)]
symbols_list.extend(random.choice('0123456789') for j in range(3))
symbols_list.extend(random.choice('!@#$%^&*') for k in range(2))
random.shuffle(symbols_list)
print("".join(symbols_list))
