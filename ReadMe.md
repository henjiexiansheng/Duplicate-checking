## 1、题目查重

### 1.1 程序执行流程

1. 导入源库数据，将源库数据生成多键字典
2. 导入新库数据，将新库数据生成多键字典
3. 将两库数据合并生成新的总库字典
4. 将三库字典去除冗余字
5. 将三库字典的键和值进行交换，交换后新的键为题目，值为学号等信息
6. 将三库字典分别进行自我比较，得出的重复信息
7. 如果存在源库字典的重复数据，则生成重复(源库数据).csv，程序跳出
8. 如果存在新库字典的重复数据，则生成重复(新库数据).csv，程序跳出
9. 如果新源两个字典均无重复数据，则判断总库字典是否有重复。
10. 如总库字典存在重复数据，则生成重复(总库数据).csv，程序跳出
11. 如果三库数据均无重复，则生成汇总文件总库数据.csv，这个文件便是最终无重复的合并数据

### 1.2 测试：源库重，新库无重

> 执行日志

![image-20210515121057961](查重作业.assets/image-20210515121057961.png)

> 重复(源库数据)-0515121028

![image-20210515121214454](查重作业.assets/image-20210515121214454.png)

### 1.3 测试：源库无重，新库重

> 执行日志

![image-20210515121443315](查重作业.assets/image-20210515121443315.png)

> 重复(新库数据)-0515121417

![image-20210515121533978](查重作业.assets/image-20210515121533978.png)

### 1.4 测试：源新均重复

> 执行日志

![image-20210515121746512](查重作业.assets/image-20210515121746512.png)

> 重复(新库数据)-0515121650

![image-20210515121820410](查重作业.assets/image-20210515121820410.png)

> 重复(源库数据)-0515121650

![image-20210515121853178](查重作业.assets/image-20210515121853178.png)

### 1.5 测试：本身无重，之间有重

> 执行日志

![image-20210515122033209](查重作业.assets/image-20210515122033209.png)

> 重复(总库数据)-0515122019

![image-20210515122104178](查重作业.assets/image-20210515122104178.png)

### 1.6 测试：三库均无重复

> 执行日志

![image-20210515122148846](查重作业.assets/image-20210515122148846.png)

> 总库数据-0515122141

![image-20210515122225472](查重作业.assets/image-20210515122225472.png)


## 2、外文查重

### 2.1 测试数据

#### 2.11 源库数据

> 待查重的各个学生的论文相关信息

![image-20210515111806829](查重作业.assets/image-20210515111806829.png)

#### 2.12 总库数据 

> 存放了入库的各个学生的论文相关信息

![image-20210515111931810](查重作业.assets/image-20210515111931810.png)

### 2.2 程序执行流程

1. 导入源库数据，将源库数据生成多键字典
2. 导入总库数据，将总库数据生成多键字典
3. 将源库数据和总库数据以==句节==为单位拆分成一个个的句子
4. 将源库的每一句话，分别放入总库中查找是否存在重复，将重复的信息单独保存
5. 计算并输出存在重复同学的重复率
6. 将重复的具体信息生成新的CSV

### 2.3 执行结果

> 重复率

![image-20210515112607167](查重作业.assets/image-20210515112607167.png)

> CSV

![image-20210515112749297](查重作业.assets/image-20210515112749297.png)

## 3、中文查重

### 3.1 测试数据

#### 3.11 源库数据

> 待查重的各个学生的论文相关信息

![image-20210515115352198](查重作业.assets/image-20210515115352198.png)

#### 3.12 总库数据

> 存放了入库的各个学生的论文相关信息

![image-20210515115450232](查重作业.assets/image-20210515115450232.png)

### 3.2 程序执行流程

1. 导入源库数据，将源库数据生成多键字典
2. 导入总库数据，将总库数据生成多键字典
3. 将源库数据和总库数据以==句节==为单位拆分成一个个的句子
4. 将源库的每一句话，分别放入总库中查找是否存在重复，将重复的信息单独保存
5. 计算并输出存在重复同学的重复率
6. 将重复的具体信息生成新的CSV

### 3.3 执行结果

> 重复率

![image-20210515115610403](查重作业.assets/image-20210515115610403.png)

> CSV

![image-20210515115643318](查重作业.assets/image-20210515115643318.png)







