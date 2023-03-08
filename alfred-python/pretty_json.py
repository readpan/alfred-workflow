#!/usr/bin/env python3
import json
import os
import sys
import time

# 获取当前时间戳
timestamp = int(time.time())

# 要写入的字符串
query = sys.argv[1]
# 找到第一个{的位置
index = query.find("{")
# 找到最后一个}的位置
index2 = query.rfind("}")
if index != -1 and index2 != -1:
    query = query[index:index2 + 1]
else:
    print(1)
json_object = json.loads(query)

query = json.dumps(json_object, indent=2)
# 构造文件路径
file_path = "/tmp/json_format/{}.json".format(timestamp)

# 如果文件夹不存在, 则创建
if not os.path.exists("/tmp/json_format"):
    os.makedirs("/tmp/json_format")
# 打开文件并写入字符串
with open(file_path, "w") as f:
    f.write(query)
    f.close()

os.system(f'open -a "Google Chrome" {file_path}')
# print(file_path)
