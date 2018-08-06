
import random
from datetime import datetime


def get_ticket():
    s = 'rqiotfdkafapotqtpojgjka2341555698'
    ticket = ''
    for i in range(20):
        ticket += random.choice(s)
    return ticket


def get_order_num():
    s = 'qwertyuiopasdfghjk123456789463'
    num = ''
    for i in range(6):
        num += random.choice(s)
    order_time = datetime.now().strftime('%Y%m%d%H%M%S')
    return order_time + num