#!/usr/bin/python3
#   multiconn-server.py

import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()
