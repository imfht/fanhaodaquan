#-*- encoding=utf8 -*-

'''
Author: d1y<chenhonzhou@gmail.com>
date: 2020-06-17
'''

import os,sys
import re
import uuid
import json
from pathlib import Path

__runScriptName = "番号大全"
__replaceName = "最新番号"

def checkDev():
  args = sys.argv
  argsLen = len(args)
  if (argsLen <= 1):
    return False 
  return args[1] == 'dev'

def getScriptDir():
  __dirname = os.path.dirname(os.getcwd())
  result = os.path.join(__dirname, __runScriptName)
  return result

def Formatting(txt):
  name = ""
  id = uuid.uuid1().hex
  Len = len(txt)
  data = []
  for index in range(Len):
    now = txt[index]
    if index == 0:
      name = now.replace(__replaceName, "", 2)
      name = name.replace("\n", "")
    else:
      i = now.find("】", 0, len(now))
      code = now[1:i]
      title = now[i+1:]
      data.append({
        "code": code,
        "title": title
      })

  return {
    "name": name,
    "id": id,
    "data": data
  }

def ReadFile(path):
  ctx = open(path, encoding="utf-8")
  txt = ctx.readlines()
  ctx.close()
  res = Formatting(txt)
  return res

# https://blog.csdn.net/zhuoyuezai/article/details/84979177
def write_list_to_json(list, json_file_save_path):
  """
  将list写入到json文件
  :param list:
  :param json_file_save_path: json文件存储路径
  :return:
  """
  try:
    # os.chdir(json_file_save_path)
    with open(json_file_save_path, 'w') as  f:
      json.dump(list, f)
  except IOError:
    print("Error: 没有找到文件或读取文件失败")
  else:
    # TODO
    pass

def ScanFile(dir = getScriptDir()):
  _lists = os.listdir(dir)
  _isDev = checkDev()
  default_loop_width = 2
  Limit = default_loop_width if _isDev else len(_lists)
  # 总数据
  datas = []
  # 女优
  actress = []
  # 所有车牌号
  codes = []
  uDir = path_utils("data.json")
  aDir = path_utils("actress.json")
  cDir = path_utils("codes.json")
  for index in range(Limit):
    current_file_name = _lists[index]
    current_file = os.path.join(dir, current_file_name)
    print("当前处理文件: ", current_file_name)
    tempData = ReadFile(current_file)
    actress.append(tempData['name'])
    datas.append(tempData)
    for i in tempData['data']:
      _n = i['code']
      codes.append(_n)

  write_list_to_json(datas, uDir)
  write_list_to_json(actress, aDir)
  write_list_to_json(codes, cDir)

def path_utils(path):
  isDev = checkDev()
  dir = getScriptDir()
  now = os.path.dirname(dir)
  proDir = os.path.join(now, "data")
  if isDev:
    proDir = os.path.join(now, "dev")
  path_auto_create(proDir)
  result = os.path.join(proDir, path)
  return result

def path_auto_create(path):
  return Path(path).mkdir(parents=True, exist_ok=True)

if __name__=="__main__":
  # TODO
  ScanFile()
  print("开始生成cdn链接..")
  os.system("node" + " file2cdn.js")
  pass