# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
Date: 2020/5/14 13:47
"""

import os
import time
import matplotlib.pyplot as plt


class CreatePie(object):

    def __init__(self, data, labels, dst, name='', title='Title', aspect=1, autopct='%0.2f%%', explode=[], shadow=True):
        """
        :param data: 饼状图使用的数据，一般为列表
        :param labels: 饼状图各个label名称，一般为列表
        :param dst: 存放生成图片的文件夹路径
        :param name: 图片的名称，默认为当前时间戳
        :param title: 图片的标题，默认为Title
        :param aspect: 图片x轴与y轴的比例，默认为1
        :param autopct: 用来在饼状图上添加格式化字符串
        :param explode: 饼状图各个饼叶偏离中心的距离占半径的比例，默认为不偏离
        :param shadaw: 是否显示阴影，默认为显示
        """
        self.data = data
        self.labels = labels
        self.dst = dst
        self.name = name if name else str(int(time.time()))
        self.title = title
        self.aspect = aspect
        self.autopct = autopct
        self.explode = explode if explode else [x * 0 for x in range(len(data))]
        self.shadow = shadow

    def drew(self):
        plt.axes(aspect=self.aspect)
        plt.pie(
            x=self.data,
            labels=self.labels,
            autopct=self.autopct,
            explode=self.explode,
            shadow=self.shadow
        )
        plt.title(self.title)
        picname = self.name + '.jpg'
        picdir = os.path.join(self.dst, picname)
        plt.savefig(picdir)
