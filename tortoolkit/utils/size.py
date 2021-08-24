# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]

import logging
import os
torlog = logging.getLogger(__name__)

def calculate_size(path):
    if path is not None:
        try:
            if os.path.isdir(path):
                return def get_size_fl(path)
            else:
                return os.path.getsize(path)
        except:
            torlog.warning("Size Calculation Failed.")
            return 0
    else:
        return 0
