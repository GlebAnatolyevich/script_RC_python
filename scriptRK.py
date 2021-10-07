#!/bin/python3
import os
import re
import datetime
from sys import argv

#########����������##########
# ���� � ������� ��-��-����
date_now=str(datetime.date.today())
#���� ������ ������ ������ ��� 1 - ����������� 7 - �����������
weekday = int(datetime.datetime.today().isoweekday())

# ���� � ������� ����� ������������ �������������� 5 - �������
arhivday = [5]
# ������� ��� ����� ������ ������ ��������� � ����������� � �����
workdays = [1,2,3,4]

# ���������� ���������� ������������
    #a,archive = argv
# ���� �� ������ ���� �������� ������ �������� ������
file_wither="/home/gleb/B/whither_path"
file_whence="/home/gleb/B/spisok_serv"
file_log="/home/gleb/B/log_backup"
#############################

def copy_file(line,file_wither,date_now):
    #print(line,file_wither,date_now)
    name_ip,path_whence = line.split(":")
    name,ip = name_ip.split("@")
    os.system("rsync -avz "+line+" "+file_wither+ip+date_now)

#copy_file("gleb@192.168.150.139:/home/gleb/OP","/home/gleb/buk/",date_now)

def arhiv_file(way):
    #print(way)
    os.chdir("/home/gleb/buk/")
    os.system("find ./ -maxdepth 1 -type d -exec tar -czf {}.tar.gz {} \;")


def write_file(date_now,path_whence,ip,result):
   # print(date_now,":",path_whence,ip)
    path=open(file_log,"w")
    path.write(date_now,":",path_whence,ip,result)
    path.close()

    #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def readint_file_wither(file_wither):
    path1=open(file_wither,"r")
    path_wither=path1.readline()
    arhiv_file(path_wither)
    path1.close()




def readint_file(file_wither,file_whence):

    path1=open(file_wither,"r")
    path2=open(file_whence,"r")
    path_wither=path1.readline()

    for line in path2.readlines():
        if line[0] != "#":
            result_line=re.sub("\n", '', line)
            result_path=re.sub("\n", '', path_wither)

            copy_file(result_line,result_path,date_now)

            path1.close()
            path2.close()

#print(readint_file(file_wither,file_whence))
####################################################

if weekday in workdays:
    readint_file(file_wither,file_whence)
if weekday in arhivday:
    readint_file_wither(file_wither)


####################################################


