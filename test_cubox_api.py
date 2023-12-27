import requests
import logging
logging.basicConfig(level=logging.DEBUG)

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

# Example usage with hypothetical values
# url_to_save = "https://www.bilibili.com/video/BV1RN411V7B9"
url_to_save = "https://developer.baidu.com/article/detail.html?id=1079288"
# title = "图片换衣项目（可以给任何人穿任何衣服）"
title = "向量检索在闲鱼：高效识别重复视频-百度开发者中心"
description = "GitHub项目地址：https://github.com/HumanAIGC/OutfitAnyone"
tags = ["example", "test/te"]
folder = "bili_collection"

# Call the function with example values
response = save_url_to_cubox(url_to_save, title, description, tags, folder)
print(response)