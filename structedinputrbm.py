import numpy

class para:
    def __init__(self, k=5, n_visible, n_hidden, numpy_rng=None, W=None):
        if numpy_rng is None:
            numpy_rng = numpy.random.RandomState(1234)


        if W is None:
            a = 1. / n_visible
            initial_W = numpy.array(numpy_rng.uniform(  # initialize W uniformly
                low=-a,
                high=a,
                size=(n_visible*k, n_hidden)))

            self.W = initial_W
            self.k=k


            
    def update_para(self, itemid, k=5, child_W):
        self.W[itemid:itemid+k]=child_W
        return self.W

    def get_para(self, itemid, k=5, n_visible)
