# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/webscraping
# blog: http://thinkdiff.net
# MIT License

# --------------------------
#  Writing Logs in File
# --------------------------

import logging

def set_custom_log_info(filename):
    logging.basicConfig(filename=filename, level=logging.INFO)
    
def report(e:Exception):
    logging.exception(str(e))

