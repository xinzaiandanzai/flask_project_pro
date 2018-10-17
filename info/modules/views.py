from flask import session, current_app

from day02.info.static import redis_store
from . import index_blu
import logging


@index_blu.route('/')
def index():
    # 向redis中保存一个值 name itcast
    redis_store.set("name", "itcast")
    logging.debug("debug")
    logging.error("error")
    logging.warning("error")
    # current_app.logger.debug("llallala")
    # session["name456"] = "张三"
    return '主页啦'
