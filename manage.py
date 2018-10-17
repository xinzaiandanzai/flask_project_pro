from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from day02.info.static import create_app, db

# manage.py是程序启动的进口，只关心启动的数据及相关参数及内容，不关心具体该功能怎样实现

# 此处会使用一个create_app的方法 就类似于工厂方法
# 此方法类似于app = Flask(__name__)


app = create_app('development')
# 命令的迁移
manager = Manager(app)
# todo 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
