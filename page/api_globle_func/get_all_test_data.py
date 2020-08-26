#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: get_test_file_path
@time: 2020/8/25 10:56
@desc: 根据globalyml配置文件获取api_auto_case的路径，根据项目名称获取测试项目project.yml配置文件路径
"""


import os
from util.sysEdit.filepathEdit import get_project_path
from util.fileEdit.get_data import getExcelData, getYamlData


def get_global_config_data():
    globle_config_path = os.path.join(get_project_path(), "config", "global.yml")
    globle_data = getYamlData(globle_config_path)[0]
    return globle_data


def get_project_config():
    globle_data = get_global_config_data()
    globle_yml_path = os.path.join(globle_data.get("data_path"),  globle_data.get("project_name"), "project.yml")
    project_config = getYamlData(globle_yml_path)[0]
    return project_config


def get_project_test_data():
    deat_save_path = get_global_config_data().get("data_path")
    project_config = get_project_config()
    project_excel = os.path.join(deat_save_path, project_config.get("save_path").get("test_case_path"))
    api_config = getExcelData(project_excel, 0)
    test_cases = getExcelData(project_excel, 1)
    project_testdatafile = os.path.join(deat_save_path, project_config.get("save_path").get("test_data_path"))
    test_data_dict = {
        "project_config": project_config,
        "api_config": api_config,
        "test_case": test_cases,
        "project_testdatafile": project_testdatafile,
    }
    return test_data_dict

