# 导入日志模块

import logging
from logging.handlers import RotatingFileHandler
from flask.ext.session import Session

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis

from config import config

# 初始化数据库
#  在Flask很多扩展里面都可以先初始化扩展的对象，然后再去调用 init_app 方法去初始化
db = SQLAlchemy()

# todo 此行代码含义
redis_store = None

def setup_log(config_name):
#     设置日志记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)
# 创建日志记录器，指明日志保存路径、每个日志文件的最大大小、保存的日志个数
    file_log_handler=RotatingFileHandler('logs/log ',maxBytes=1024*1024*100,backupCount=10)


# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
#    记录日志的格式，日志等级，输入日志信息的文件名 行数 日志信息
    file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象(flask app使用的)添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name):
#     配置日志，并且传入配置名字，以便能获取到指定配置锁对应的日志等级
    setup_log(config_name)
    # 创建flask对象
    app=Flask(__name__)
#     加载配置
    app.config.from_object(config[config_name])
# 通过app初试化
    db.init_app(app)
#     初始化redis存储对象
    global redis_store
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启当前项目 CSRF 保护，只做服务器验证功能
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)
#   注册蓝图
    from day02.info.modules.views import index_blu
    app.register_blueprint(index_blu)
    return app

