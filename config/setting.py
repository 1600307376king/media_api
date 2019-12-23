# session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

server_list = {
    'development': {
        'port': '5000',
        'ip': '127.0.0.1',
        'url': 'http://127.0.0.1:5000',
        'debug': True,
    },
    'production_setting': {
        'port': '80',
        'ip': 'www.exp1727.cn',
        'url': 'http://www.exp1727.cn:80',
        'debug': False,
    },
    'test_setting': {
        'port': '8099',
        'ip': 'www.exp1727.cn',
        'url': 'http://www.exp1727.cn:8099',
        'debug': True,
    }
}

ENV_NAME = 'development'
SERVER_PORT = server_list[ENV_NAME]['port']
IP = server_list[ENV_NAME]['ip']
URL = server_list[ENV_NAME]['url']

DEBUG = server_list[ENV_NAME]['debug']