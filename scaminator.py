import requests
from faker import Faker
import threading
import random
import time

fake = Faker()

num_thread = 20
url = ''
data = {
    'email': '',
    'password': '',
}

print('Thanks for using me to beat the scammer!')


def do_request():
    while True:
        length_password = random.randint(8, 24)
        fake_data = {
            'email': fake.email(),
            'password': fake.password(length=length_password)
        }
        request_data = {**data, **fake_data}
        response = requests.post(url, data=request_data).status_code
        print(response)
        print(fake_data)
        time.sleep(1)


threads = []

print('Try to start ' + str(num_thread) + ' threads....')

for i in range(num_thread):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)
    print('Thread ' + str(i + 1) + ' created.')

for i in range(num_thread):
    threads[i].start()
    print('Thread ' + str(i + 1) + ' started.')

for i in range(num_thread):
    threads[i].join()
    print('Thread ' + str(i + 1) + ' joined.')
