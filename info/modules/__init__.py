from flask import Blueprint
# 创建蓝图 对象
index_blu=Blueprint('index',__name__)
from . import views