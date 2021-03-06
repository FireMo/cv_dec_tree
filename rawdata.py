# encoding=utf-8


# 获取训练集数据
def get_train_data(train_filename):
    # fr = open('xiguadata4utf8.txt')
    with open('./dataDir/sample_data1/' + train_filename) as fr:
    # with open('./dataDir/zhongxiguadata.txt') as fr:
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    return lenses


# 获取所有的属性值并组装成字典
def get_more_train_data():
    with open('xiguadata4utf8.txt') as fm:
        lenses_more = [inst.strip().split('\t') for inst in fm.readlines()]
    return lenses_more

# 获取属性列表
def get_attr_value():
    # fp = open('xigualabel2.txt')
    with open('labelxigua.txt') as fp:
        lenses_labelses = [inst.strip().split('\t') for inst in fp.readlines()]
    lenses_labels = lenses_labelses[0]
    # lensesLables = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
    # lensesLablestwo = lensesLables[:]
    # lensesLables = ['seze', 'gendi', 'qiaosheng', 'wenli', 'qibu', 'chugan']
    return lenses_labels


# 获取测试集数据
def get_test_data(test_filename):
    with open('./dataDir/sample_data1/' + test_filename) as fp:
        lenses_test = [inst.strip().split('\t') for inst in fp.readlines()]
    return lenses_test


# 将数据集的数组组装成标签
# def data_deal(lenses, lenses_labels):
def data_deal():
    data_dict = {}
    lenses = get_more_train_data()
    lenses_labels = get_attr_value()
    for i in range(len(lenses_labels)):
        lab_list = set([example[i] for example in lenses])
        data_dict[lenses_labels[i]] = lab_list
    return data_dict
