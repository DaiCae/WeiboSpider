import logging
import yaml
from flask import Flask

from common import blueprint
from common import register


def create_app():
    app = Flask(__name__)
    # 加载配置文件
    app.config.update(yaml.full_load(open('config.yml', 'r')))
    blueprint.init(app)
    register.init(app)
    return app


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')
    analyze_app = create_app()
    analyze_app.run(host='0.0.0.0', debug=True, port=5002)


