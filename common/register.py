import nacos
import threading


class Register:
    NACOS_ADDRESS = None
    SERVICE_IP = None
    SERVICE_PORT = None
    SERVICE_NAME = None

    @classmethod
    def read_config(cls, app):
        cls.NACOS_ADDRESS = app.config['NACOS_ADDRESS']
        cls.SERVICE_IP = app.config['SERVICE_IP']
        cls.SERVICE_PORT = app.config['SERVICE_PORT']
        cls.SERVICE_NAME = app.config['SERVICE_NAME']

    @classmethod
    def service_register(cls):
        client = nacos.NacosClient(cls.NACOS_ADDRESS)
        client.add_naming_instance(cls.SERVICE_NAME, cls.SERVICE_IP, cls.SERVICE_PORT)
        threading.Timer(5, cls.service_register).start()


def init(app):
    Register.read_config(app)
    threading.Thread(target=Register.service_register, daemon=True).start()
