# ZhDate 中国农历日期处理对象

[![VersionBadge](https://img.shields.io/pypi/v/zhdate.svg?style=flat)](https://pypi.org/project/zhdate/)  [![pythonversion](https://img.shields.io/pypi/pyversions/zhdate.svg?style=flat-square)](https://pypi.org/project/zhdate/) [![LicenseBadge](https://img.shields.io/github/license/CutePandaSh/zhdate.svg?style=flat)](https://github.com/CutePandaSh/zhdate/blob/master/LICENSE)

不用网络接口直接本地计算中国农历，支持农历阳历互转

## 安装方法

通过 pip 直接安装

```bash
pip install zhdate
```

或从git拉取

```bash
git clone https://github.com/CutePandaSh/zhdate.git
cd zhdate
python setup.py install
```

更新

```bash
pip install zhdate --upgrade
```

## 使用方法

见如下代码案例:

```python
from zhdate import ZhDate

date1 = ZhDate(2010, 1, 1) # 新建农历 2010年正月初一 的日期对象
print(date1)  # 直接返回农历日期字符串
dt_date1 = date1.to_datetime() # 农历转换成阳历日期 datetime 类型

dt_date2 = datetime(2010, 2, 6)
date2 = ZhDate.from_datetime(dt_date2) # 从阳历日期转换成农历日期对象

date3 = ZhDate(2020, 4, 30, leap_month=True) # 新建农历 2020年闰4月30日
print(date3.to_datetime())

# 支持比较
if ZhDate(2019, 1, 1) == ZhDate.from_datetime(datetime(2019, 2, 5)):
    pass

# 减法支持
new_zhdate = ZhDate(2019, 1, 1) - 30  #减整数，得到差额天数的新农历对象
new_zhdate2 = ZhDate(2019, 1, 1) - ZhDate(2018, 1, 1) #两个zhdate对象相减得到两个农历日期的差额
new_zhdate3 = ZhDate(2019, 1, 1) - datetime(2019, 1, 1) # 减去阳历日期，得到农历日期和阳历日期之间的天数差额

# 加法支持
new_zhdate4 = ZhDate(2019, 1, 1) + 30 # 加整数返回相隔天数以后的新农历对象

# 中文输出
new_zhdate5 = ZhDate(2019, 1, 1)
print(new_zhdate5.chinese())

# 当天的农历日期
ZhDate.today()
```