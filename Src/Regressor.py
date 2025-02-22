import numpy as np
import abc



class Regressor(metaclass=abc.ABCMeta):
    def __init__(self, num_features):
        self._num_features = num_features   # number of features


    ## Model Tools
    @abc.abstractmethod
    def getPrediction(self, x):
        pass


    @abc.abstractmethod
    def updateParameters(self, x_batch, z_batch, batch_size, lr, loss_type):
        pass
    

    @abc.abstractmethod
    def resetWeights(self):
        pass


    @abc.abstractmethod
    def getWeights(self):
        pass
