import time
import requests
import numpy as np
from flask import Flask, jsonify

def experience_score(A,B,T,N):
    A = 0.56
    B = 0.44
    T = float(T)
    N = float(N)
    E = A * np.log10(T/5) + B * np.log10(N/500)
    return E

def Historic_score(X,Y):
    X = float(X)
    Y = float(Y)
    H = (1 - X/Y)
    return H

def certik_AUR_score():
    weight_e=0.7
    weight_h=0.3
    server_address = "http://gelei:8080"
    api_endpoint = "/api"
    A = 0.56
    B = 0.44
    try:
        # 发送 GET 请求获取数据
        response = requests.get(server_address + api_endpoint)
        if response.status_code == 200:
            # 解析 JSON 数据
            data = response.json()
            # 提取 certik 字段中的值
            certik_value = data['T']['time']
            certik_value1 = data['N']['amount']
            certik_value2 = data['X']['bug']
            certik_value3 = data['Y']['event']
            # 打印提取的值
            S1 = certik_value
            S2 = certik_value1
            S3 = certik_value2
            S4 = certik_value3

        else:
            print("请求失败，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求异常:", e)
    # 调用 experience_score 函数获取经验评分
    E = experience_score(A,B,S1,S2)
    # 调用 Historic_score 函数获取历史评分
    H = Historic_score(S3,S4)
    # 计算 AUR 评分
    total_score = 100 * (weight_e * E + weight_h * H)
    
    return total_score

def Chainsecurity_AUR_score():
    weight_e=0.7
    weight_h=0.3
    server_address = "http://gelei:8080"
    api_endpoint = "/api"
    A = 0.56
    B = 0.44
    try:
        # 发送 GET 请求获取数据
        response = requests.get(server_address + api_endpoint)
        if response.status_code == 200:
            # 解析 JSON 数据
            data = response.json()
            # 提取 certik 字段中的值
            certik_value = data['T']['time1']
            certik_value1 = data['N']['amount1']
            certik_value2 = data['X']['bug1']
            certik_value3 = data['Y']['event1']
            # 打印提取的值
            S1 = certik_value
            S2 = certik_value1
            S3 = certik_value2
            S4 = certik_value3

        else:
            print("请求失败，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求异常:", e)
    # 调用 experience_score 函数获取经验评分
    E = experience_score(A,B,S1,S2)
    # 调用 Historic_score 函数获取历史评分
    H = Historic_score(S3,S4)
    # 计算 AUR 评分
    total_score = 100 * (weight_e * E + weight_h * H)
    
    return total_score

def Hacken_AUR_score():
    weight_e=0.7
    weight_h=0.3
    server_address = "http://gelei:8080"
    api_endpoint = "/api"
    A = 0.56
    B = 0.44
    try:
        # 发送 GET 请求获取数据
        response = requests.get(server_address + api_endpoint)
        if response.status_code == 200:
            # 解析 JSON 数据
            data = response.json()
            # 提取 certik 字段中的值
            certik_value = data['T']['time2']
            certik_value1 = data['N']['amount2']
            certik_value2 = data['X']['bug2']
            certik_value3 = data['Y']['event2']
            # 打印提取的值
            S1 = certik_value
            S2 = certik_value1
            S3 = certik_value2
            S4 = certik_value3

        else:
            print("请求失败，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求异常:", e)
    # 调用 experience_score 函数获取经验评分
    E = experience_score(A,B,S1,S2)
    # 调用 Historic_score 函数获取历史评分
    H = Historic_score(S3,S4)
    # 计算 AUR 评分
    total_score = 100 * (weight_e * E + weight_h * H)
    
    return total_score

def defisafety_AUR_score():
    weight_e=0.7
    weight_h=0.3
    server_address = "http://gelei:8080"
    api_endpoint = "/api"
    A = 0.56
    B = 0.44
    try:
        # 发送 GET 请求获取数据
        response = requests.get(server_address + api_endpoint)
        if response.status_code == 200:
            # 解析 JSON 数据
            data = response.json()
            # 提取 certik 字段中的值
            certik_value = data['T']['time3']
            certik_value1 = data['N']['amount3']
            certik_value2 = data['X']['bug3']
            certik_value3 = data['Y']['event3']
            # 打印提取的值
            S1 = certik_value
            S2 = certik_value1
            S3 = certik_value2
            S4 = certik_value3

        else:
            print("请求失败，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求异常:", e)
    # 调用 experience_score 函数获取经验评分
    E = experience_score(A,B,S1,S2)
    # 调用 Historic_score 函数获取历史评分
    H = Historic_score(S3,S4)
    # 计算 AUR 评分
    total_score = 100 * (weight_e * E + weight_h * H)
    
    return total_score
Chainsecurity_AUR_score()
Hacken_AUR_score()
defisafety_AUR_score()
certik_AUR_score()