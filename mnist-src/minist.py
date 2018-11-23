import pickle,gzip,numpy

# 读取数据集
f=gzip.open('mnist-data/mnist.pkl.gz','rb')
train_set, valid_set, test_set=pickle.load(f,encoding='iso-8859-1')
f.close()


def shared_dataset(data_xy):
    """ 这是一个将数据集读取为共享变量的函数.
    我们将数据集保存为共享变量的目的是为了让Theano 将我们的代码复制到GPU 的内存当中(当代码执行在 GPU 上的时候).
    因为将整个数据集复制到 GPU 的内存里是比较缓慢的,因此我们需要将数据集分成几个不同的 minibatch 来复制,
    减少系统资源的负荷,若不这么做,系统很容易因为高负荷运行出现一个系统错误.
    """
    data_x,data_y = data_xy
    shared_x = theano.shared(numpy.asarray(data_x,dtype=theano.config.floatX))
    shared_y = thenao.shared(numpy.asarray(data_y,dtype=theano.config.floatX))

    # 当我们把数据保存到 GPU 内存的时候,数据必须是 float类型的.
    # 因此我们将标签数据也保存为`floatX`` .
    # 但是在计算过程中,我们仍然需要把它们作为整数来使用(我们将标签作为索引来使用,然后不存在也不可能拿 float 做索引的.)
    # 因此我们并不会直接返回一个 shared_y 的值,而是将这个变量转化为 整数类型再返回.
    # 这个小小的技巧就可以避免上面说的麻烦.
    return shared_x, T.cast(shared_y,'int32')