import pickle,gzip,numpy

# 读取数据集
f=gzip.open('mnist-data/mnist.pkl.gz','rb')
train_set, valid_set, test_set=pickle.load(f,encoding='iso-8859-1')
f.close()