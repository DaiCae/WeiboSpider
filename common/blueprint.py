import importlib
import os


# 自动注册蓝图
def init(app):
    for d in os.listdir('service/'):
        if d.endswith("_service.py"):
            services = importlib.import_module('service.' + d.replace('.py', ''))
            for obj in dir(services):
                if obj.endswith('_bp'):
                    # 读取蓝图对象
                    blueprint_object = getattr(services, obj)
                    app.register_blueprint(blueprint_object)
