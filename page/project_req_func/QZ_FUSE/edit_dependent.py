#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: edit_dependent
@time: 2020/8/26 17:13
@desc: 
"""
import os

from page.project_req_func.QZ_FUSE.jiemi_response import response_jiemi_dict
from util.sysEdit.filepathEdit import get_project_path
from util.data_type_data.edit_json import dict_to_json_write_file, json_file_to_dict, jiexi_json, json_to_dict


dependent_dir = os.path.join(get_project_path(), "dependent", "fpt")


def api_all_add_dependent(api_all):
    file_name = api_all.get("dependent_case_id") + ".json"
    file_path = os.path.join(dependent_dir, file_name)
    dependent_dict = json_file_to_dict(file_path)
    api_all.update(dependent_dict)
    return api_all


def save_dependent(api_all, response):
    file_name = api_all.get("case_id") + ".json"
    file_path = os.path.join(dependent_dir, file_name)
    res_jiemi_dict = response_jiemi_dict(response)
    request_dict = json_to_dict(api_all.get("data"))
    request_data_dict = {
        "SBLX": jiexi_json(request_dict, "REQUEST_COMMON_FPKJ.SBLX"),
        "KPZDDM": jiexi_json(request_dict, "REQUEST_COMMON_FPKJ.KPZDDM"),
        "FPLXDM": jiexi_json(request_dict, "REQUEST_COMMON_FPKJ.FPLXDM"),
        "KPLX": jiexi_json(request_dict, "REQUEST_COMMON_FPKJ.KPLX"),
        "ZSFS": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.ZSFS"),
        "NSRSBH": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.NSRSBH"),
        "XSF_NSRSBH": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.XSF_NSRSBH"),
        "XSF_MC": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.XSF_MC"),
        "XSF_DZDH": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.XSF_DZDH"),
        "XSF_YHZH": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.XSF_YHZH"),
        "GMF_NSRSBH": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.GMF_NSRSBH"),
        "GMF_MC": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.GMF_MC"),
        "GMF_DZDH": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.GMF_DZDH"),
        "GMF_SJH": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.GMF_SJH"),
        "GMF_DZYX": jiexi_json(res_jiemi_dict, "REQUEST_COMMON_FPKJ.GMF_DZYX"),
    }

    response_data_dict = {
        "FPQQLSH": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.FPQQLSH"),
        "FPLXDM": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.FPLXDM"),
        "FP_DM": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.FP_DM"),
        "FP_HM": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.FP_HM"),
        "KPRQ": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.KPRQ"),
        "JYM": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.JYM"),
        "PDF_URL": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.PDF_URL"),
        "OFD_URL": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.OFD_URL"),
        "SP_URL": jiexi_json(res_jiemi_dict, "interface.data.content.DATA.SP_URL")
    }
    save_data_dict = {}
    save_data_dict.update(request_data_dict)
    save_data_dict.update(response_data_dict)
    dict_to_json_write_file(file_path, save_data_dict)