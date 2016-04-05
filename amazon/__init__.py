#!/usr/bin/env
# -*- coding: utf-8 -*-
from amazon.api import *
import logging


try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
