# -*- coding: utf-8 -*-
"""
    flask
    ~~~~~
    一个基于Werkzeug的微框架，被广泛使用，并遵循最佳实践
    A microframework based on Werkzeug.  It's extensively documented
    and follows best practice patterns.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.13-dev'

# 我们从Werkzeug和Jinja2导入的这些模块并没有使用，但是作为公共接口导出。
# utilities we import from Werkzeug and Jinja2 that are unused
# in the module but are exported as public interface.
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from jinja2 import Markup, escape

from .app import Flask, Request, Response
from .config import Config
from .helpers import url_for, flash, send_file, send_from_directory, \
     get_flashed_messages, get_template_attribute, make_response, safe_join, \
     stream_with_context
from .globals import current_app, g, request, session, _request_ctx_stack, \
     _app_ctx_stack
from .ctx import has_request_context, has_app_context, \
     after_this_request, copy_current_request_context
from .blueprints import Blueprint
from .templating import render_template, render_template_string

# the signals
from .signals import signals_available, template_rendered, request_started, \
     request_finished, got_request_exception, request_tearing_down, \
     appcontext_tearing_down, appcontext_pushed, \
     appcontext_popped, message_flashed, before_render_template

# 我们并没有公开实际的JSON模块，但更方便的包装了它。
# We're not exposing the actual json module but a convenient wrapper around
# it.
from . import json

# 这是flask在json这个点导出的唯一的接口，而且有一个更通用的名字。
# This was the only thing that Flask used to export at one point and it had
# a more generic name.
jsonify = json.jsonify

# 向后兼容，在1.0中消失
# backwards compat, goes away in 1.0
from .sessions import SecureCookieSession as Session
json_available = True
