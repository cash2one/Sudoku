#coding:utf-8

__author__ = 'Administrator'

from func import *
from CrackWebSudoku import *


if __name__=="__main__":

    map_list = read_saved_maps(
        map_data_set_file = file('map_data_set.txt','r')
    )

    main_test(map_list)