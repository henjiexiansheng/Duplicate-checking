import csv          # 导入csv处理模块
import time         # 导入时间模块

titleRes = {}       # 用于存储源库原始数据
titleNew = {}       # 用于存储新库原始数据
titleSumCon = {}    # 用于存储两个库原始汇总数据

# 导入源库中数据
with open("D:/桌面/py/作业（4-28）/中文题目（原始数据无重复）.csv","r") as fpRes:
    readerRes = csv.reader(fpRes)
    next(readerRes)            # 指针往下移动1位，就是不处理表头
    for rows in readerRes:
        snoResTemp = rows[1]      # 取学号数据
        snameResTemp = rows[2]    # 取姓名数据
        titleResTemp = rows[3]    # 取题目数据
        # 解决数据合并时空行的问题
        if not bool(snoResTemp) and not bool(snameResTemp) and not bool(titleResTemp):
            continue
        titleRes[(snoResTemp,snameResTemp)] = titleResTemp  # 以多键对一值的方式存入字典

# 导入新库中数据
with open("D:/桌面/py/作业（4-28）/毕设题目（新库数据无重复）.csv","r",encoding='gb18030') as fpNew:
    readerNew = csv.reader(fpNew)
    next(readerNew)            # 指针往下移动1位，就是不处理表头
    for rows in readerNew:
        snoNewTemp = rows[4]        # 取学号数据
        snameNewTemp = rows[2]      # 取姓名数据
        titleNewTemp = rows[5]      # 取题目数据
        if not bool(snoNewTemp) and not bool(snameNewTemp) and not bool(titleNewTemp):
            continue
        titleNew[(snoNewTemp,snameNewTemp)] = titleNewTemp

# 导入两库的原始数据
titleSumCon.update(titleRes)
titleSumCon.update(titleNew)

# 去掉多余的字
titleMoRes = titleRes.copy()       # 用于存储旧库去冗余后的数据
titleMoNew = titleNew.copy()       # 用于存储新库去冗余后的数据
titleMoSum = {}                    # 用于存储两个库去冗余字后的汇总数据
for keyRes in titleMoRes:
    for i in "的地'相关''系统的设计与实现'":
        titleMoRes[keyRes] = titleMoRes[keyRes].replace(i,"")
for keyNew in titleMoNew:
    for i in "的地'相关''系统的设计与实现'":
        titleMoNew[keyNew] = titleMoNew[keyNew].replace(i,"")
titleMoSum.update(titleMoRes)      # 汇总旧库中去冗余的数据
titleMoSum.update(titleMoNew)      # 汇总新库中去冗余的数据

# 键值交换功能
queryRes = {}  # 存储交换后源库数据
queryNew = {}  # 存储交换后新库数据
querySum = {}  # 存储交换后汇总数据
for keyRes,valueRes in titleMoRes.items():   # 遍历字典中返回的键和值
        queryRes.setdefault(valueRes,[]).append(keyRes) # 设置query的键为titleMo的值，query的值为titleMo的键
for keyNew,valueNew in titleMoNew.items():   # 遍历字典中返回的键和值
        queryNew.setdefault(valueNew,[]).append(keyNew)
for keySum,valueSum in titleMoSum.items():   # 遍历字典中返回的键和值
        querySum.setdefault(valueSum,[]).append(keySum)

#提取重复的键值对
lsRes = {}  # 存取源库中的重复数据
lsNew = {}  # 存取新库中的重复数据
lsSum = {}  # 存取汇总后的重复数据
for keyRes in queryRes.keys():            # 遍历薪字典中的key（书名）
    if len(queryRes[keyRes]) > 1:         # 如果key的值（学号）有多个
        for i in queryRes[keyRes]:        # 遍历这些个值（学号）
            print("【Error】源库学号为：",i,"，重复的书籍名为：",titleRes[i]) # 打印问题学生的学号和题目
            lsRes[i] = titleRes[i]
for keyNew in queryNew.keys():  # 遍历薪字典中的key（书名）
    if len(queryNew[keyNew]) > 1:         # 如果key的值（学号）有多个
        for i in queryNew[keyNew]:        # 遍历这些个值（学号）
            print("【Error】新库学号为：",i,"，重复的书籍名为：",titleNew[i]) # 打印问题学生的学号和题目
            lsNew[i] = titleNew[i]
for keySum in querySum.keys():  # 遍历薪字典中的key（书名）
    if len(querySum[keySum]) > 1:         # 如果key的值（学号）有多个
        for i in querySum[keySum]:        # 遍历这些个值（学号）
            print("【Error】总库学号为：",i,"，重复的书籍名为：",titleSumCon[i]) # 打印问题学生的学号和题目
            lsSum[i] = titleMoSum[i]

# 将重复的源库数据写入对应的CSV
time = time.strftime("%m%d%H%M%S", time.localtime(time.time()))  # 获取当前系统时间，并把获取的时间转换成"年月日格式”
if not bool(lsRes):
    print("【Info】源库数据无重复！")
else:
    count = 0
    f = open("D:/桌面/py/作业（4-28）/重复(源库数据)-"+time+".csv", "w")
    f.write("序号,学号,姓名,重复题目\n")
    for row in lsRes.items():
        count = count + 1
        seqRow = (str(count),row[0][0],row[0][1],row[1])
        f.write(",".join(seqRow) + "\n")
    else:
        print("【Error】发现重复题目，请查看：重复(源库数据)!")
    f.close()

# 将重复的新库数据写入对应的CSV
if not bool(lsNew):
    print("【Info】新库数据无重复！")
else:
    count = 0;
    f = open("D:/桌面/py/作业（4-28）/重复(新库数据)-"+time+".csv", "w")
    f.write("序号,学号,姓名,重复题目\n")
    for row in lsNew.items():
        count = count + 1
        newRow = (str(count),row[0][0],row[0][1],row[1])
        f.write(",".join(newRow) + "\n")        # 将序列seqRow以逗号分隔输出，末尾换行
    else:
        print("【Error】发现重复题目，请查看：重复(新库数据)!")
    f.close()

# 判断汇总数据条件是否成立，成立生成汇总CSV，否则提示修改数据
if not bool(lsRes) and not bool(lsNew):
    count = 0
    if not bool(lsSum):
        f = open("D:/桌面/py/作业（4-28）/总库数据-" + time + ".csv", "w")
        f.write("序号,学号,姓名,论文题目\n")
        for row in titleSumCon.items():
            count = count + 1
            sumConRow = (str(count), row[0][0], row[0][1], row[1])
            f.write(",".join(sumConRow) + "\n")
        else:
            print("【Info】恭喜您，数据无异常，成功导出：总库数据!")
    else:
        f = open("D:/桌面/py/作业（4-28）/重复(总库数据)-"+time+".csv", "w")
        f.write("序号,学号,姓名,重复题目\n")
        for row in lsSum.items():
            count = count + 1
            sumRow = (str(count), row[0][0], row[0][1], row[1])
            f.write(",".join(sumRow) + "\n")
        else:
            print("【Error】发现重复题目，请查看：重复(总库数据)!")
else:
    print("【Error】因存在重复数据，无法生成总库，请更正后再试！")





