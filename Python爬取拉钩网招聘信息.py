# -*- coding: utf-8 -*-
#Python爬取拉钩网招聘信息
import requests
from openpyxl import Workbook

new_url = 'http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

def get_json(url, page, lang_name):
    '''解析json，取得需要的信息'''
    data = {'first': 'true', 'pn': page, 'kd': lang_name}
    json = requests.post(url, data).json()
    list_con = json['content']['positionResult']['result']
    info_list = []
    for i in list_con:
        info = []
        info.append(i['companyShortName'])
        info.append(i['companyFullName'])
        info.append(str(i['companyLabelList']))
        info.append(i['salary'])
        info.append(i['city'])
        info.append(i['companySize'])
        info.append(i['education'])
        info_list.append(info)
    return info_list

def main():
    lang_name = input('职位名： ')
    page = 1
    url = new_url
    info_result = []
    while page < 31:
        info = get_json(url, page, lang_name)
        info_result += info
        page += 1
    wb = Workbook()
    ws1 = wb.active
    ws1.title = lang_name
    for row in info_result:
        ws1.append(row)
    wb.save('职位信息.xlsx')
    print('完成！！')

if __name__ == '__main__':
    main()
