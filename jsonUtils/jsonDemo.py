#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 16:57 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : jsonDemo.py 
# @Software: PyCharm Community Edition
import json
import logging


def load_valid_json(json_str):
    """
    ---------------------------------------------------------------------
    Function Name: load_valid_json
    Description:   Check the string and transfer it to json objects
    Input  : String
    Output : Json object
    """
    try:
        if isinstance(json_str, dict):
            return json_str
        elif json_str is not None and json_str.strip() != "":
            json_obj = json.loads(json_str)
        else:
            logging.error("Json String is Null to be loaded")
            return None
    except Exception as e:
        logging.error("Load json failed, err = %s" % e.args[0])
        return None
    else:
        # Return the sequence if it is valid
        return json_obj

