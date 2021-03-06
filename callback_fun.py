# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 00:48:07 2021

@author: Maysam
"""

from tensorflow.keras.callbacks import Callback
import time

class TimeHistory(Callback):
    def on_train_begin(self, logs={}):
        self.times = []

    def on_epoch_begin(self, batch, logs={}):
        self.epoch_time_start = time.time()

    def on_epoch_end(self, batch, logs={}):
        self.times.append(time.time() - self.epoch_time_start)
        
