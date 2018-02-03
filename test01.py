# -*- coding:utf8 -*-
import crossv
import trees
import rawdata
import treePlotter
import os
# basedir = os.path.abspath(os.path.dirname(__file__))


# 构建决策树
def create_tree():
    # lenses_lables = get_attr()
    lenses = rawdata.get_train_data()
    lenses_lables = rawdata.get_attr_value()
    lenses_two = lenses[:]
    dec_tree = trees.createTree(lenses, lenses_lables)
    return dec_tree


# lenses_tree = create_tree()
# print treePlotter.createPlot(lenses_tree)
# 列出windows目录下的所有文件和文件名
# for (root, dirs, files) in os.walk("./dataDir/sample_data1"):
#     for filename in files:
#         # print os.path.join(root, filename)
#         # print os.path.join(filename)
#         with open('./dataDir/sample_data1/' + os.path.join(filename)) as fn:
#             lenses = [inst.strip().split('\t') for inst in fn.readlines()]
#         # print lenses
#         # print '----------'
#
#     # 遍历子文件夹
#     for dirc in dirs:
#         print os.path.join(root, dirc)
#         # print '****'

# 获取属性列表
lenses_labels = rawdata.get_attr_value()

dirs = os.listdir('./dataDir/sample_data1')
# print type(dirs)
decision_trees = []
accuracies = []

tests = dirs[:5]  # 测试集
trains = dirs[-5:]  # 训练集
for i in range(len(trains)):
    # with open('./dataDir/sample_data1/' + trains[i]) as fr:
    #     lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    # lenses_two = lenses[:]
    # lenses_labels_two = lenses_labels[:]
    lenses = rawdata.get_train_data(trains[i])
    decision_tree = trees.createTree(lenses, lenses_labels)
    # print treePlotter.createPlot(decision_tree)  # 循环打印决策树
    decision_trees.append(decision_tree)
# print len(decision_trees)  # 5
# print treePlotter.createPlot(decision_trees)
for m in range(len(tests)):
    accu = []
    decs_tree = decision_trees[m]
    test_data = rawdata.get_test_data(tests[m])
    # print decs_tree  # 决策树
    # print test_data  # 被测数据
    for y in range(len(test_data)):
        result = trees.classify(decs_tree, lenses_labels, test_data[y][:-1])
        # print '结果：%s' % result
        # print '循环次数：%d' % y
        accu.append(result)

    # print '数组长度：%d' % len(accu)
    # print '*****'
    accuracies.append(accu)
# print len(accuracies)
# print accuracies[-1][-4]
print len(accuracies)
print '华丽的分割线'


test_labs = []
for p in range(len(tests)):
    test_lab = []
    test_data = rawdata.get_test_data(tests[p])
    for t in range(len(test_data)):
        test_lab.append(test_data[t][-1])
    test_labs.append(test_lab)
# print test_labs[4][0]
print len(test_labs)
print '又一个华丽的分割线'


for w in range(len(tests)):
    count = 0.0
    for q in range(len(test_labs[w])):

        print '真实标签值为：%s; 决策树检测的标签为：%s' % (test_labs[w][q], accuracies[w][q])
        if test_labs[w][q] == accuracies[w][q]:
            count += 1
    print '正确率为：%f' % (count/(len(test_labs[w])))
    print '又又一个华丽的分割线'
















# 验证精度
# def is_accuracy():
#     # 构建决策树
#     lenses_tree = create_tree()
#     accuracy = []
#     # 属性值
#     # lenses = rawdata.get_train_data()
#     lenses_lables = rawdata.get_attr_value()
#     lenses_test = rawdata.get_test_data(test_filename=None)
#     print lenses_test[-1]
#     for n in range(len(lenses_test)):
#         result = trees.classify(lenses_tree, lenses_lables, lenses_test[n][:len(lenses_test[n])-1])
#         accuracy.append(result)
#     return accuracy


# 测试集结果
# def last_result():
#     count = 0.0
#     lenses_test = rawdata.get_test_data()
#     lc = is_accuracy()
#     for y in range(len(lc)):
#         print '验证集中数据标签为：' + lenses_test[y][-1]
#         print '决策树验证结果为：' + lc[y]
#         print '*****'
#         if lc[y] == lenses_test[y][-1]:
#             count += 1
#     # print count
#     print '验证集精度为：%f' % (count/(len(lc)))
#     print 'lc'

