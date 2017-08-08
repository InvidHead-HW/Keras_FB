# -*- coding: utf-8 -*-
#Original Author: QuantumLiu
#https://github.com/QuantumLiu/wechat_callback/blob/master/wechat_utils.py
#Modified by Kotobuki
from keras import __version__ as kv
kv=int(kv[0])
import platform
pv=int(platform.python_version()[0])
import numpy as np
import scipy.io as sio
from keras.callbacks import Callback
import time
import matplotlib  
matplotlib.use('Agg') # 
import matplotlib.pyplot as plt
from math import ceil

if pv>2:
    import _thread as th
else:
    import thread as th
import os
from os import system
import re
import traceback
import platform
from requests.exceptions import ConnectionError
from fbchat import Client
from fbchat.models import *




def send_text(text):
    try:
        client.sendMessage(text, thread_id=client.uid, thread_type=ThreadType.USER)
        return
    except (ConnectionError,NotImplementedError,KeyError):
        traceback.print_exc()
        print('\nConection error,failed to send the message!\n')
        return
    else:
        return
def send_img(filename):
    try:
        client.sendLocalImage(filename, thread_id=client.uid, thread_type=ThreadType.USER)
        return
    except (ConnectionError,NotImplementedError,KeyError):
        traceback.print_exc()
        print('\nConection error,failed to send the figure!\n')
        return
    else:
        return


class sendmessage(Callback):

    def __init__(self,savelog=True,fexten='',username="",password=""):
        self.username=username
        self.password=password
        self.fexten=(fexten if fexten else '')#the name of log and figure files 
        self.savelog=bool(savelog)#save log or not
        global client
        client = Client(username, password)
    def t_send(self,msg):
        try:
            send_text(msg)
            return
        except (ConnectionError,NotImplementedError,KeyError):
            traceback.print_exc()
            print('\nConection error,failed to send the message!\n')
            return
        else:
            return
    def t_send_img(self,filename):
        try:
            send_img(filename)
            return
        except (ConnectionError,NotImplementedError,KeyError):
            traceback.print_exc()
            print('\nConection error,failed to send the figure!\n')
            return
        else:
            return
       
            
    def shutdown(self,sec,save=True,filepath='temp.h5'):
        if save:
            self.model.save(filepath, overwrite=True)
            self.t_send('Command accepted,the model has already been saved,shutting down the computer....')
        else:
            self.t_send('Command accepted,shutting down the computer....')
        if 'Windows' in platform.system():
            th.start_new_thread(system, ('shutdown -s -t %d' %sec,))
        else:
            m=(int(sec/60) if int(sec/60) else 1)
            th.start_new_thread(system, ('shutdown -h -t %d' %m,))
            
        

    def cancel(self):
        #Cancel function to cancel shutting down the computer
        self.t_send('Command accepted,cancel shutting down the computer....')
        if 'Windows' in platform.system():
            th.start_new_thread(system, ('shutdown -a',))
        else:
            th.start_new_thread(system, ('shutdown -c',))
        

    def GetMiddleStr(self,content,startStr,endStr):
        #get the string between two specified strings
        #从指定的字符串之间截取字符串
        try:
          startIndex = content.index(startStr)
          if startIndex>=0:
            startIndex += len(startStr)
          endIndex = content.index(endStr)
          return content[startIndex:endIndex]
        except:
            return ''


    def validateTitle(self,title):
        #transform a string to a validate filename
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
        new_title = re.sub(rstr, "", title).replace(' ','')
        return new_title
        

    def prog(self):#Show progress
        nb_batches_total=(self.params['nb_epoch'] if not kv-1 else self.params['epochs'])*self.params['nb_sample']/self.params['batch_size']
        nb_batches_epoch=self.params['nb_sample']/self.params['batch_size']
        prog_total=(self.t_batches/nb_batches_total if nb_batches_total else 0)+0.01
        prog_epoch=(self.c_batches/nb_batches_epoch if nb_batches_epoch else 0)+0.01
        if self.t_epochs:
            now=time.time()
            t_mean=float(sum(self.t_epochs)) / len(self.t_epochs)
            eta_t=(now-self.train_start)*((1/prog_total)-1)
            eta_e=t_mean*(1-prog_epoch)
            t_end=time.asctime(time.localtime(now+eta_t))
            e_end=time.asctime(time.localtime(now+eta_e))
            m='\nTotal:\nProg:'+str(prog_total*100.)[:5]+'%\nEpoch:'+str(self.epoch[-1])+'/'+str(self.stopped_epoch)+'\nETA:'+str(eta_t)[:8]+'sec\nTrain will be finished at '+t_end+'\nCurrent epoch:\nPROG:'+str(prog_epoch*100.)[:5]+'%\nETA:'+str(eta_e)[:8]+'sec\nCurrent epoch will be finished at '+e_end
            self.t_send(m)
            print(m)
        else:
            now=time.time()
            eta_t=(now-self.train_start)*((1/prog_total)-1)
            eta_e=(now-self.train_start)*((1/prog_epoch)-1)
            t_end=time.asctime(time.localtime(now+eta_t))
            e_end=time.asctime(time.localtime(now+eta_e))
            m='\nTotal:\nProg:'+str(prog_total*100.)[:5]+'%\nEpoch:'+str(len(self.epoch))+'/'+str(self.stopped_epoch)+'\nETA:'+str(eta_t)[:8]+'sec\nTrain will be finished at '+t_end+'\nCurrent epoch:\nPROG:'+str(prog_epoch*100.)[:5]+'%\nETA:'+str(eta_e)[:8]+'sec\nCurrent epoch will be finished at '+e_end
            self.t_send(m)
            print(m)
            

