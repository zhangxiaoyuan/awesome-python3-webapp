#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Jagger'

'''
async web application.
'''

import logging; 
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body=b'<html><body><h1>Awesome</h1><p>This is awesome-python3-webapp</p></body></html>', content_type='text/html')


@asyncio.coroutine
def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000....')
	return srv


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(init(loop))
	loop.run_forever()
