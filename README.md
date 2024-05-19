# Welcome to CC-Monitor!
CC-Monitor是跨链安全监控的评分系统小工具，能帮助用户实时监控跨链dapp的安全性，并且在某跨链dapp安全评分低于阙值时发出警告通过邮件等形式

CC-Monitor对于一个跨链dapp的安全性研究分别从三个地方考量了dapp的安全性
1：智能合约的审计方面
2：节点的去中心化程度
3：审计公司的可靠性
我们选择三个方向去评估一个跨链dapp的安全性，并且将数据量化为数学模型，直观的让用户感受到



#  CC-Monitor  数学算法
## 节点的去中心化程度
引入基尼系数(Gini Coefficient)来衡量节点分布的不均匀性,基尼系数越小表示分布越均匀
基尼系数的计算公式为:
Gini = sum(i=1 to m) sum(j=1 to m) |distribution[i] - distribution[j]| / (2 * m^2 * mean(distribution))
当gini越接近1时去中心化程度越高

## 智能合约审计公司可靠性
A与B是权重系数
T为审计公司的成立时间长度
N为审计公司审计过的合约数量

S = Alog(1+T/5) + Blog(N/500)

## 对跨链dapp的评分
该方法从各大审计公司如certik等，获取其对dapp的评分标准，为了更准确，我们采用了多个数据源的办法确保dapp评分的真实性

F(s) = F(e) * 0.54 + F(h) * 0.46
