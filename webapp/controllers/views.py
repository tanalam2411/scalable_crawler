#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tornado.web


class ParseUrlHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        