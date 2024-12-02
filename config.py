import random
import string

password = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(20, 40))])

TOKEN = ""