#-*-coding=utf-8-*-
import os
#�г�ĳ���ļ����µ�����case�������õ���python
#����py�ļ�����һ�κ������һ��pyc�ĸ���
caselist=os.listdir("C:\\Users\\neunn\\Documents\\wushixin\\eclipse_job\\workspaces\\PythonCase\\src\\Python27\\test_case")
for a in caselist:
    s=a.split('.')[1]   #ѡȡ��׺��Ϊpy���ļ�
    if s=='py':
        #�˴�ִ��dos�����������浽log.txt
        os.system('C:\\Users\\neunn\\Documents\\wushixin\\eclipse_job\\workspaces\\PythonCase\\src\\Python27\\test_case\\%s 1>>log.txt 2>&1' %a)
        