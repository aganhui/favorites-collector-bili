import json
import sys
sys.path.append("../..")
# import myopenai
from common import *

def print_json_structure(obj, indent=0):
    for key, value in obj.items() if isinstance(obj, dict) else enumerate(obj):
        print('  ' * indent + str(key), end=': ')
        if isinstance(value, (dict, list)):
            print()
            print_json_structure(value, indent + 1)
        else:
            print(value)
            # print()
            pass

path_json = "/mnt/e/data/collection/收藏夹信息/默认收藏夹.json"

with open(path_json, 'r', encoding='utf-8') as f:
    path_json = f.read()
    data = json.loads(path_json)
    # print(len(data))
    # print(data.keys())

def transform_dict(data):
    return [ {
        "title": obj["视频信息"]["标题"], 
        "description": obj["视频信息"]["简介"],
        } for obj in data.values() ]

def add_tag(data, tag):
    idx = 0
    for obj in data.values():
        if idx >= len(tag):
            break
        obj["视频信息"]["标签"] = tag[idx]
        idx += 1

idx = 0
for i in data.keys():
    if idx > 0:
        break
    # print(i)
    # print(data[i])
    print_json_structure(data[i])
    # print(dict2markdown(data[i]))
    idx += 1

# data_llm_input = transform_dict(data)
# print(len(data_llm_input))
# data_llm_input = data_llm_input[:100]
# data_llm_output = myopenai.get_llm_response(TAG_PROMPT + "\n" + json.dumps(data_llm_input, ensure_ascii=False, indent=4), "gpt-4-1106-preview")
# data_llm_output = json.loads(data_llm_output)
# # print(data_llm_output)
# add_tag(data, data_llm_output)
# # print(data[:5])

# idx = 0
# for i in data.keys():
#     if idx > 0:
#         break
#     # print(i)
#     # print(data[i])
#     print_json_structure(data[i])
#     # print(dict2markdown(data[i]))
#     idx += 1

# path_json_out = "/mnt/e/data/collection/收藏夹信息/默认收藏夹_tags.json"
# with open(path_json_out, 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
