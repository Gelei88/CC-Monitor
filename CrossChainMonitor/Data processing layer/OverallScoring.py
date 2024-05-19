import requests
import time

def certik_score():
    server_address = "http://gelei:8000"
    api_endpoint = "/api"
    while True:
        try:
            # 发送 GET 请求获取数据
            response = requests.get(server_address + api_endpoint)
            if response.status_code == 200:
                # 解析 JSON 数据
                data = response.json()
                # 提取 certik 字段中的值
                certik_value = data['certik']['AAVE']
                S1 = certik_value
                print(S1)
            else:
                print("请求失败，状态码：", response.status_code)
        except requests.exceptions.RequestException as e:
            print("请求异常:", e)
            
            
        # 等待一分钟
        time.sleep(20)

def Chainsecurity_score():
    server_address = "http://gelei:8000"
    api_endpoint = "/api"

    while True:
        try:
            # 发送 GET 请求获取数据
            response = requests.get(server_address + api_endpoint)
            if response.status_code == 200:
                # 解析 JSON 数据
                data = response.json()
                # 提取 certik 字段中的值
                certik_value = data['Chainsecurity']['AAVE']
                S2 = certik_value
            else:
                print("请求失败，状态码：", response.status_code)
        except requests.exceptions.RequestException as e:
            print("请求异常:", e)
            return S2
            
        # 等待一分钟
        time.sleep(20)
def Hacken_score():
    server_address = "http://gelei:8000"
    api_endpoint = "/api"
    while True:
        try:
            # 发送 GET 请求获取数据
            response = requests.get(server_address + api_endpoint)
            if response.status_code == 200:
                # 解析 JSON 数据
                data = response.json()
                # 提取 certik 字段中的值
                certik_value = data['Hacken']['AAVE']
                S3 = certik_value
            else:
                print("请求失败，状态码：", response.status_code)
        except requests.exceptions.RequestException as e:
            print("请求异常:", e)
            return S3
            
        # 等待一分钟
        time.sleep(20)

def defisafety_score():
    server_address = "http://gelei:8000"
    api_endpoint = "/api"

    while True:
        try:
            # 发送 GET 请求获取数据
            response = requests.get(server_address + api_endpoint)
            if response.status_code == 200:
                # 解析 JSON 数据
                data = response.json()
                # 提取 certik 字段中的值
                certik_value = data['defisafety']['AAVE']
                S4 = certik_value
            else:
                print("请求失败，状态码：", response.status_code)
        except requests.exceptions.RequestException as e:
            print("请求异常:", e)
            return S4
            
        # 等待一分钟
        time.sleep(20)