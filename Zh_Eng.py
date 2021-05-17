import csv
import time
# 导入新库中数据
titleEngRes = {}    # 存放源库数据
titleEngSum = {}    # 存放总库数据
queryEngSum = {}    # 存放合并后的总库段落
lsEngSum = {}       # 存放重复的论文信息
str1 = ""           # 将数据转换成字符串
queryResEngSum = {}    # 拆分成句子后的源库数据

# 提取源库数据
time = time.strftime("%m%d%H%M%S", time.localtime(time.time()))  # 获取当前系统时间，并把获取的时间转换成"年月日格式”
with open("D:/桌面/py/作业（4-28）/外文查重（源库数据）.csv","r") as fpEng:
    readerEng = csv.reader(fpEng)
    next(readerEng)
    for rows in readerEng:
        snoEngResTemp = rows[0]         # 提取学号
        snameEngResTemp = rows[1]       # 提取姓名
        snameEngTitleResTemp = rows[2]  # 提取论文题目
        resKeytemp = snoEngResTemp+","+snameEngResTemp+","+snameEngTitleResTemp # 将学号，姓名，题目拼接成串
        titleEngRes.setdefault(resKeytemp,[]).append(rows[3])   # 将同一个姓名下的所有段落整合成1篇文章
    for key in titleEngRes.keys():
        for i in titleEngRes[key]:
            str1 = str1 + str(i)    # 将同一键下的所有内容（一个个字符串）拼接成一个大字符串
        queryResEngSum[key] = str1.split(".").copy()   # 将文章拆分成以句子为单位的1个个列表赋予新的字典
        queryResEngSum[key].pop()                      # 去掉首尾多余的空格
        str1 = ""
#print(lsResEngSum) # 测试：lsResEngSum存放了各个键下面对应的各个句子的字符串

# 提取总库数据
str1 = ""
with open("D:/桌面/py/作业（4-28）/外文查重（总库数据）.csv","r") as fpEng:
    readerEng = csv.reader(fpEng)
    next(readerEng)
    for rows in readerEng:
        snoEngSumTemp = rows[0] # 提取总库学号作为键
        titleEngSum.setdefault(snoEngSumTemp, []).append(rows[3])
        # print(titleEngRes.keys(),"\n")
    for key in titleEngSum.keys():
        for i in titleEngSum[key]:
            str1 = str1 + str(i)  # 将同一键下的所有内容（一个个字符串）拼接成一个大字符串
        queryEngSum[key] = str1.split(".").copy() # 将同一个学号下的所有段落整合成1篇文章
        queryEngSum[key].pop() # 去除首位空格
        str1 = ""
#print(lsEngSum)  # 测试：lsEngSum字典中存放了每个学号下的，各个句子的字符串

# 内容查重
for resKey in queryResEngSum.keys():       # 遍历源库字典的各个键
    for res in queryResEngSum[resKey]:     # 遍历源库中各个键对应的所有句子
        #print("[源库数据]",res,"\n\n\n") # 测试：查询源库输出的各个语句
        for sumKey in queryEngSum.keys():
            for sum in queryEngSum[sumKey]:
                #print("[总库数据]",sum,"\n\n\n") # 测试：查询源库输出的1个语句后，总库输出的所有语句（源库中的每个语句都需要跟总库的所有语句比对）
                if res == sum:
                    lsEngSum.setdefault(resKey,[]).append(res)  # 将重复的数据存入lsEngSum

# 计算重复率
for resKey in queryResEngSum.keys():       # 遍历源库所有键
    for lsEngKey in lsEngSum.keys():    # 遍历重复库中的所有键
        if resKey in lsEngKey:
            resLen = len(queryResEngSum[resKey])   # 存在重复的论文全部句子个数
            lsLen = len(lsEngSum[lsEngKey])     # 存在重复的论文重复句子个数
            print("[Warning]",resKey,"存在重复,论文重复率为：",'{:.2%}'.format(lsLen / resLen))

# 生成详细重复内容的csv
with open("D:/桌面/py/作业（4-28）/重复(外文数据)-"+time+".csv", "w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["学号","姓名","题目","重复句子"])
    for rowKey in lsEngSum.keys():
        rowKeyList = str(rowKey).split(",").copy()
        for rowValue in lsEngSum[rowKey]:
            new = [rowKeyList[0],rowKeyList[1],rowKeyList[2],rowValue]
            writer.writerow(new)
    else:
        print("[Warning]重复(外文数据)生成成功！ ")
