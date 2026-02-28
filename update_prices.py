import json
import requests
import re

# 1. 定义我们要抓取的官方链接
URLS = {
    "kling": "https://klingai.com/cn/dev/pricing",
    "doubao": "https://www.volcengine.com/docs/82379/1544106"
}

def fetch_kling_price():
    # 这里是一个示例逻辑：模拟访问可灵页面
    # 注意：真实爬虫需要根据页面HTML标签进行精调
    try:
        # 假设我们抓取到了 1.5 这个数字
        return 1.5 
    except:
        return None

def update_json():
    # 读取你现有的 prices.json
    with open('prices.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 模拟更新逻辑
    new_price = fetch_kling_price()
    if new_price:
        for model in data['models']:
            if model['official_id'] == 'kling-v2-6':
                model['price'] = new_price
                print(f"更新成功：可灵价格已调整为 {new_price}")

    # 保存回文件
    with open('prices.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    update_json()
