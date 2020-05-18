# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
Date: 2020/5/16 15:14
"""

import csv


def csv_read(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, dialect='excel')
        for row in reader:
            data.append(row)
    return data


def csv_write(path, data):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        for row in data:
            writer.writerow(row)
    return True


def csv_dict_write(path, head, data):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, head)
        writer.writeheader()
        writer.writerows(data)
    return True


def csv_dict_read(path, key):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, dialect='excel')
        for row in reader:
            data.append(row[key])
    return data
