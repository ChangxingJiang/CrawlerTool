import random
from datetime import datetime


def console(string: str, sign: str = None):
    """输出格式化信息到控制台

    格式样例: 2020-06-08 09:09:40 [sign] string

    :param string 输出信息
    :param sign 输出标记（可选）
    """
    if sign:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [" + sign + "] " + string)
    else:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + string)


def get_scope_random(num, scope=0.2):
    """生成散布于期望值附近的随机数

    :param num: 期望值
    :param scope: 随机散布范围: 取值范围为[0,1],默认值为0.2(若不再取值范围内则使用默认值)
    """
    if not 0 <= scope <= 1:
        scope = 0.2
    return random.uniform((1 - scope) * float(num), (1 + scope) * float(num))
