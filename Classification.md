分类和预测
===

#概念

*    分类：预测分类标号（离散、无序）
*    预测：简历连续值函数模型


#分类步骤

*    学习：建立描述预先定义的数据类或者概念集的分类器
*    分类：通过分析或从训练集学习来构造分类器


#聚类和分类
>由于提供了每个训练元组的类标号，这一步也称作监督学习，不同于无监督学习（聚类），每个训练元组的类标号未知，学习的类的个数也未知

#检验集
>分类效果检验如果使用训练集合来测量，结果可能是乐观，因为分类器趋向于过分拟合数据，因此需要使用检验集

#预测步骤

*    建模
*    预测


#分类和预测的数据预处理

*    数据清理：减少噪声、处理缺失值
*    相关分析：？
*    数据变换和规约

#分类效果的评估标准

*    准确率
*    速度
*    鲁棒性
*    可伸缩性
*    可解释性

#主要算法

##决策树归纳

###伪代码

    args: D, attribute_list, Attribute_Selection_Method
    return: Decision-Tree
    time complexity: O(n * |D| * log(|D|))
    
    GDT(D, attribute_list)
    1    Create New Node N
    2    if all elements in D is Same Type C:
    3        return N as leaf node, mark type as C;
    4    if attribute_list is empty:
    5        return N as leaf Node, mark D as Common Type
    6    splitting_criterion = Attribute_Selection_Method
    7    Mark N as splitting node as splitting_criterion
    8    if splitting_attribute is Discrete && allow multiple split
    9        attribute_list = attribute_list - splitting_attribute
    10   for output in splitting_criterion:
    11       if Dj is empty:
    12           add a leaf node on N
    13           marked as common type in D
    14       else:
    15           add sub Node GTD(Dj, attribute_list)
    16   return N;
          
    

###属性选择度量(Attribute-Selection-Method)

>将给定的类标记的训练元组的数据划分 D『最好』地分成个体类的启发式方法，假设数据集D 为训练集，假定类标号属性具有 m 个不同值，定义 m 个不同的类Ci(i = 1, ...., m). 设 C(i,d) 是 D 中 Ci 类的集合

####信息增益
    
    Info(D) = -Sum(pi * log(pi) / log2)
    pi 为 D 中任意元组属于 Ci 的概率，用|C(i, d)| / |D| 估算

####增益率

    SplitInfo(A, D) = - Sum(|Dj| / |D|) * log(2, |Dj| / |D|)
    GainRatio(A) = Gain(A) / SplitInfo(A)

####Gini指标

	Gini(D) = 1 - Sum(pi * pi)
	Gini(A, D) = |D1| / |D| * Gini(D1) + |D2| / |D| * Gini(D2)

###剪枝



###可伸缩性

##贝叶斯分类

###贝叶斯定理

###朴素贝叶斯分类