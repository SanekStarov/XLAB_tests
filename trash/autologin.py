import redis
import time
from random import randint

host = ''
port = 0000
password = ''

client = redis.Redis(host=host, port=port, password=password)


def random_phone_num_generator():
    first = str(randint(902, 921)).zfill(2)
    second = str(randint(100, 888)).zfill(3)
    last = str(randint(1000, 9998)).zfill(4)
    return '{}{}{}'.format(first, second, last)


def get_code(phone: str):
    value = client.get(phone)
    if value:
        value = value.decode("utf-8")
    return value

if __name__ == "__main__":
    phone = random_phone_num_generator()
    print(phone)
    time.sleep(15)
    password=get_code(phone)
    print(str(password))