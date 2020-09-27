from nb_log import LogManager

import datetime
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR,'logs\\')

def log(text):
    now = datetime.datetime.now().strftime('%Y%m%d-%H%M')
    logger = LogManager('INFO').get_logger_and_add_handlers(is_add_stream_handler=True,do_not_use_color_handler=True,
                                                log_filename=LOG_PATH+now+'.log')
    logger.info(text)

if __name__ == '__main__':
    log('日志开始')
