"""
add random data for testing purpose
"""

import os
import django
import random
import string
from datetime import datetime

# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')  # 把 your_project 替换成你的项目名称
django.setup()

from goods.models import Goods  # 把 your_app 替换成你的应用名称

# 生成随机字符串作为商品名称
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# 生成随机价格
def random_price():
    return round(random.uniform(1, 1000), 2)

# 生成随机描述
def random_description():
    return random_string(random.randint(20, 100))

# 添加若干测试数据
for i in range(10):  # 这里可以修改要添加的数据数量
    name = random_string(random.randint(5, 20))
    price = random_price()
    description = random_description()
    print(f'name: {name}, price: {price}, description: {description}')
    Goods.objects.create(name=name, price=price, description=description)

print("测试数据添加成功！")