#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os,sys
import re
from xlwt import *

pattern_begin = r'.*\[WEB\] network request url=(?P<url>.*)\.\(tm=(?P<tm>\d+).*'
pattern_end = r'.*\[WEB\] network finish url=(?P<url>.*),\(tm=(?P<tm>\d+),(?P<spend>\d+).*'

p_begin = re.compile(pattern_begin)
p_end = re.compile(pattern_end)

records_dic_list = {}

def fileProc(f):
    for line in f.readlines():
        m_begin = p_begin.match(line)
        m_end = p_end.match(line)
        if m_begin != None:
            records_dic = {}
            url = m_begin.group('url')
            tm =  m_begin.group('tm')
            records_dic['url'] = url
            records_dic['start_time'] = tm
            records_dic_list[url] = records_dic
        if m_end != None:
            url = m_end.group('url')
            tm = m_end.group('tm')
            spend = m_end.group('spend')
            if url in records_dic_list:
                records_dic_list[url]['end_time'] = tm
                records_dic_list[url]['spend'] = spend
            else:pass

def writeExcel():
    w = Workbook()
    ws = w.add_sheet('advanced')
    i = 1
    ws.write(0, 0,'url')
    ws.write(0, 1, 'start time')
    ws.write(0, 2, 'end_time')
    ws.write(0, 3, 'spend')
    for (k,v) in records_dic_list.items():
        ws.write(i, 0, k.split('/')[-1].split('?')[0])
        ws.write(i, 1, v['start_time'] if 'start_time' in v else 'none')
        ws.write(i, 2, v['end_time'] if 'end_time' in v else 'none')
        ws.write(i, 3, v['spend'] if 'spend' in v else 'none')
        i += 1
    w.save('advanced.xls')

def run():
    if len(sys.argv) < 2:
        print 'Please input file!'

    f = file('advanced.log')
    #f = file('advanced.log')
    fileProc(f)
    f.close()
    writeExcel()

if __name__ == '__main__':
    print 'running...'
    run()
    print 'end!'