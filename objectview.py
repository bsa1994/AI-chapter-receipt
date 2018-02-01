# !/usr/bin/python
# coding: utf-8

class ObjectView(object):
    """ View objects as dicts """

    def __init__(self, d):
        """
        :param d: {}
            Object data
        """

        self.__dict__ = d
