#!/usr/bin/env python
# coding=utf-8

"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os


from util.fileEdit.ymalEdit.readYmal import YamlReader
from util.fileEdit.excel.read_data import ExcelReader


def getYamlData(file):
    """
    传入ymal文件路径，读取ymal的数据
    :param file:
    :return:
    """
    yamlData = YamlReader(file).data
    return yamlData


def getExcelData(file, sheet, isdict=True):
    """
    传入Excel文件路径，sheet，读取Excel的数据
    :param file: Excel文件路径
    :param sheet: 表的id或者名称
    :param isdict: True返回字典，false返回list
    :return:
    """
    excelData = ExcelReader(file, sheet, isdict).data
    return excelData



