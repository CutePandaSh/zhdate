'''
-*- coding: utf-8 -*-
File: zhdate.py
File Created: Sunday, 17th February 2019 4:58:02 pm
Author: Wang, Yi (denniswangyi@gmail.com)
'''
'''
changed: Saturday, 21st January 2023
by: Eilles Wan (EillesWan@outlook.com)
'''

__version__ = "1.0"
__all__ = [
    
    # 主要类
    "ZhDate",

    # 主要常量
    "LUNARYEARCODE",
    "LUNARNEWYEAR",
]


from .main import ZhDate, LUNARYEARCODE, LUNARNEWYEAR
