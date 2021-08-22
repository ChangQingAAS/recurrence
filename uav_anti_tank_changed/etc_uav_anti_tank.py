import torch
import os

app_abspath = os.path.dirname(__file__)
#USE_CUDA = torch.cuda.is_available()
USE_CUDA = False
device = torch.device("cuda" if USE_CUDA else "cpu")

SERVER_IP = "127.0.0.1"  # 仿真服务器IP地址
SERVER_PORT = "6060"  # 仿真服务器端口号
SERVER_PLAT = "windows"  # windows linux
SCENARIO_NAME = "uav_anti_tank_changed.scen"  # 想定名称
SIMULATE_COMPRESSION = 4  #推演档位:即推演速度
#SYNCHRONOUS = True # True同步, False异步 # todo: 测试这个参数是什么

SHOW_FIGURE = True  # 这个参数是不是能做成false，但是还是要连墨子AI啊

# 这个参数从20000改到100
target_radius = 100.0
target_name = "坦克排(T-72 MBT x 4)"

task_end_point = {}
task_end_point["latitude"] = 44.44 #这个应该是根据起点和障碍位置定的
task_end_point["longitude"] = 33.33

# todo: 这几个mode也要试一下
# app_mode:
# 1--local windows train mode
# 2--local linux train mode
# 3--remote windows evaluate mode
# 4--local windows evaluate mode
app_mode = 1

MAX_EPISODES = 5000  # 一共训练多少会和
MAX_BUFFER = 10000
MAX_STEPS = 30  # 每回合一共做多少次决策
DURATION_INTERVAL = 120  # 仿真时间多长做一次决策。（单位：秒）# 这个应该和想定文件里给的推演速度有关
#######################

#######################
TMP_PATH = "%s/%s/tmp" % (app_abspath, SCENARIO_NAME)
OUTPUT_PATH = "%s/%s/output" % (app_abspath, SCENARIO_NAME)  # 多了一层目录

MODELS_PATH = "%s/Models/" % OUTPUT_PATH  # 模型输出路径
#######################
