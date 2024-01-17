import requests
import json
# import logging
# logging.basicConfig(level=logging.DEBUG)

def save_url_to_cubox(url, title, description, tags, folder):
    """
    Save a URL to Cubox using the provided API.
    
    Parameters:
    - api_key: The API key for authentication
    - url: The URL to save
    - title: The title of the item
    - description: The description of the item
    - tags: A list of tags
    - folder: The folder to save the item in
    
    Returns:
    - response: The response from the API call
    """
    
    # Endpoint from the API documentation
    endpoint = "https://cubox.pro/c/api/save/a0uuqw7rU9i"
    
    # # Headers to include the API key
    # headers = {
    #     "Authorization": f"Token {api_key}"
    # }
    
    # Data to be sent in the POST request
    data = {
        "type": "url",
        "content": url,
        "title": title,
        "description": description,
        "tags": tags,
        "folder": folder
    }
    
    # Make the POST request
    # Note: This is commented out because we cannot make external requests here.
    # response = requests.post(endpoint, headers=headers, json=data)
    response = requests.post(endpoint, json=data, verify=False)
    
    # Normally you would return the response from the POST request.
    # Here we return the data and headers that would be used in the request.
    return response

path_json = "/mnt/e/data/collection/收藏夹信息/默认收藏夹.json"

def transform_dict(data):
    return [ {
        "url": "https://www.bilibili.com/video/" + obj["BV"],
        "title": obj["视频信息"]["标题"], 
        "description": obj["视频信息"]["简介"],
        "tags": [
            "bili-publish/publish-" + obj["三个时间"]["发布时间"].split(" ")[0], 
            "bili-collect/collect-" + obj["三个时间"]["收藏时间"].split(" ")[0]
            ],
        "folder": "bili_collection",
        } for obj in data.values() ]

def send_urls_from_json(path_json):
    with open(path_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data_dict = transform_dict(data)
    for idx in range(len(data_dict)):
        # if idx > 3:
        #     break
        tmp = data_dict[idx]
        url_to_save, title, description, tags, folder = tmp["url"], tmp["title"], tmp["description"], tmp["tags"], tmp["folder"]
        response = save_url_to_cubox(url_to_save, title, description, tags, folder)
        if response.status_code != 200:
            print("send to cubox error: ", idx)

path_new_json = "/mnt/e/data/collection/收藏夹信息/默认收藏夹.json"
path_new_json = "/mnt/e/data/collection/收藏夹信息/默认收藏夹_new_2023-12-27_22-33-00.json"
# send_urls_from_json(path_new_json)