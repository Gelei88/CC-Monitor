import time
import requests
import numpy as np
from flask import Flask, jsonify

def decentralization_score(n, distribution):
    
    # 归一化处理
    distribution = [x / sum(distribution) for x in distribution]
    
    # 计算基尼系数
    m = len(distribution)
    mean_dist = sum(distribution) / m
    gini = 0
    for i in range(m):
        for j in range(m):
            gini += abs(distribution[i] - distribution[j])
    gini /= 2 * m**2 * mean_dist
    
    # 计算去中心化程度
    score = 100 *(1 - gini)
 
    return score
