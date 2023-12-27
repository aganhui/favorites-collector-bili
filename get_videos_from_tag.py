import json


base_link = "https://www.bilibili.com/video/"
def dict2markdown(obj):
    str_md = "* [{}]({})".format(obj["视频信息"]["标题"], base_link + obj["BV"])
    str_md_suffix = "    * up: {}; 发布时间: {}; 播放量: {}; 时长: {}".format(obj["up主"]["昵称"], obj["三个时间"]["发布时间"], obj["观众数据"]["播放量"], obj["视频信息"]["时长"])
    new_line = "\n        * "
    str_md_suffix2 = "    * 简介: {}{}".format(new_line, obj["视频信息"]["简介"].replace("\n", new_line))
    return str_md + "\n" + str_md_suffix + "\n" + str_md_suffix2

path_json = "/mnt/e/data/collection/收藏夹信息/默认收藏夹_tags.json"
with open(path_json, 'r', encoding='utf-8') as f:
    path_json = f.read()
    data = json.loads(path_json)

tag = {"all": []}    # 不同的key对应不同的select任务，列表中的tag表示挑出来的视频需要包含的标签

# obj["视频信息"]["标签"]是个标签列表，如果tag是obj["视频信息"]["标签"]的子集，就会被挑出来
def obj_match_tag(obj, tag):
    for t in tag:
        if "标签" not in obj["视频信息"] or obj["视频信息"]["标签"] is None:
            return False
        if t not in obj["视频信息"]["标签"] and t.lower() not in obj["视频信息"]["标签"]:
            return False
    return True

selected_data = {}
for k, v in tag.items():
    selected_data[k] = []
    for obj in data.values():
        # obj的标签中包含v中的所有元素就会被挑出来
        if obj_match_tag(obj, v):
            selected_data[k].append(obj)

# 将selected_data中的每个视频数据转换为markdown格式，然后写入文件
path_md_base = "/mnt/e/data/collection/收藏夹信息/默认收藏夹_{}_{}.md"
for k, v in selected_data.items():
    path_md = path_md_base.format(k, "-".join(tag[k]))
    with open(path_md, 'w', encoding='utf-8') as f:
        for obj in v:
            f.write(dict2markdown(obj) + "\n\n")

