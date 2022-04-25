# -*- coding: utf-8 -*-
# @Time : 2021/11/10 18:28
# @Author : chenxuan


import pandas as pd
from faker import Faker
import datetime
import random

# 设置字段
for i in range(1, 19):
    exec('x' + str(i) + '=[]')


def randomNum(N):
    random_number = random.sample('0123456789', N)
    return ''.join(random_number)


def add_customer(num):
    fake = Faker("zh_CN")  # 初始化，可生成中文数据

    # 设置样本
    id = 'TKB'
    intent_type = ['二手房', '新房']  # 房源意向类型
    buy_type = ['买', '卖', '租']  # 买卖意向
    intent_city = ['广州市']  # 意向城市
    intent_area = ['越秀区', '荔湾区', '天河区', '海珠区', '白云区']  # 意向区域
    intent_business_district = {'越秀区': ['东川路', '解放南', '越秀南'], '荔湾区': ['芳村', '西关', '菊树'],
                                '天河区': ['龙口东', '粤垦', '华景新城'], '海珠区': ['中大', '赤岗', '滨江东'], '白云区': ['江高镇', '大金钟路', '新市']}
    intent_garden = ['测试小区1', '测试小区2', '测试小区3']
    intent_price = [200, 300, 400]
    house_area = [70, 80, 90]
    intent_unit = [2, 3]
    intent_source = ['移动', '联通', '电信']  # 电话来源
    grab_way = ['http', 'APP', 'http/APP']  # 潜客抓取方式
    specific_way = ['IM', '电话', '弹窗', '预约', 'IM/电话', 'IM/电话/弹窗', 'IM/电话/弹窗/预约']  # 潜客抓取具体方式

    # 循环生成数据20行，具体多少行可以根据需求修改
    for i in range(num):
        date = '2021' + fake.date()[4:]
        x1.append(id + randomNum(6))
        x2.append(fake.phone_number())
        x3.append(fake.name())
        x4.append('广东广州')
        x5.append(random.choice(intent_type))
        x6.append(random.choice(buy_type))
        x7.append(random.choice(intent_city))
        area = random.choice(intent_area)
        area1 = intent_business_district.get(area)
        x8.append(area)
        x9.append(random.choice(area1))
        x10.append(random.choice(intent_garden))
        x11.append(random.choice(intent_price))
        x12.append(random.choice(house_area))
        x13.append(random.choice(intent_unit))
        x14.append(date)
        x15.append(random.choice(intent_source))
        x16.append(random.choice(grab_way))
        x17.append(random.choice(specific_way))
        x18.append(None)

    # 创建数据表
    datas1 = pd.DataFrame({
        'id': x1,
        '手机号码': x2,
        '姓名': x3,
        '号码归属地': x4
    })

    datas2 = pd.DataFrame({
        'id': x1,
        '意向类型': x5,
        '客户意向': x6,
        '意向城市': x7,
        '意向区域': x8,
        '意向商圈': x9,
        '意向小区': x10,
        '意向价格': x11,
        '意向面积': x12,
        '意向户型': x13,
        '意向日期': x14,
        '意向来源': x15,
        '抓取方式': x16,
        '具体方式': x17,
        '加分项': x18
    })

    # DataFrame类的to_csv()方法输出数据内容，不保存行索引和列名
    datas1.to_excel(r'data/test1.xlsx', encoding='utf-8', index=False)
    datas2.to_excel(r'data/test2.xlsx', encoding='utf-8', index=False)


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    add_customer(21)
    endtime = datetime.datetime.now()
    print(f'生成{21}条数据一共花了:{(endtime - starttime).seconds}秒')
