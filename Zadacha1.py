# Задача 1: Логирование с использованием нескольких файлов
import logging

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    debug_info_handler = logging.FileHandler("debug_info.log")
    debug_info_handler.setLevel(logging.DEBUG)
    debug_info_handler.setFormatter(formatter)
    logger.addHandler(debug_info_handler)
    
    warning_errors_handler = logging.FileHandler("warning_errors.log")
    warning_errors_handler.setLevel(logging.WARNING)
    warning_errors_handler.setFormatter(formatter)
    logger.addHandler(warning_errors_handler)
    
    return logger

def main_logging():
    logger = setup_logging()
    logger.debug('This message is  DEBUG.')
    logger.info('This message is INFO.')
    logger.warning('This message is WARNING.')
    logger.error('This message is ERROR.')
    logger.critical('This message is CRITICAL.')
    

    for handler in logger.handlers:
        handler.close()

if __name__ == "__main__":
    main_logging()
