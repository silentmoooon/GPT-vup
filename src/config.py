"""
 @Author: jiran
 @Email: jiran214@qq.com
 @FileName: config.py
 @DateTime: 2023/4/7 14:30
 @SoftWare: PyCharm
"""
import configparser
import json
import os.path


file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')

_config = configparser.RawConfigParser()
_config.read(file_path)

tss_settings = dict(_config.items('edge-tts'))

api_key = _config.get('openai', 'api_key')
temperature = _config.get('openai', 'temperature')
room_id = _config.getint('room', 'id')
mysql = dict(_config.items('mysql'))
milvus = dict(_config.items('milvus'))
debug = _config.getboolean('other', 'debug')
proxy = _config.get('other', 'proxy')

action_plugin = _config.getboolean('plugin', 'action')
schedule_plugin = _config.getboolean('plugin', 'schedule')
speech_plugin = _config.getboolean('plugin', 'speech')
context_plugin = _config.getboolean('plugin', 'context')

try:
    live2D_actions = []
    live2D_embeddings = []
    live2D_action_dict= []
    if action_plugin:
        with open("./action.json", 'r') as load_f:
            live2D_action_dict = json.load(load_f)
        live2D_actions = live2D_action_dict.keys()
        live2D_embeddings = [live2D_action_dict[action] for action in live2D_actions]
except Exception as e:
    print('读取embedding文件错误，请检查本地是否生成action.json 且动作不为空， 使用action plugin前请先运行 python manager.py action', e)

if __name__ == '__main__':
    print(api_key, proxy)