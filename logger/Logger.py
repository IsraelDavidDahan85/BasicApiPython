import os
import logging
import datetime
import socket
from pythonjsonlogger import jsonlogger

DEFAULT_LOG_LEVEL = 'INFO'
HOST = socket.gethostname()


class Logger():
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        level = getattr(logging, os.getenv('LOG_LEVEL', DEFAULT_LOG_LEVEL).upper())
        self.logger.setLevel(level)
        log_handler = logging.StreamHandler()
        formatter = CustomJsonFormatter()
        log_handler.setFormatter(formatter)
        self.logger.addHandler(log_handler)

    def debug(self, msg, **kwargs):
        ex = {}
        for key, value in kwargs.items():
            ex[key] = value
        self.logger.debug(msg, extra=ex, stacklevel=2)

    def info(self, msg, **kwargs):
        ex = {}
        for key, value in kwargs.items():
            ex[key] = value
        self.logger.info(msg, extra=ex, stacklevel=2)

    def warning(self, msg, **kwargs):
        ex = {}
        for key, value in kwargs.items():
            ex[key] = value
        self.logger.warning(msg, extra=ex, stacklevel=2)

    def error(self, msg, **kwargs):
        ex = {}
        for key, value in kwargs.items():
            ex[key] = value
        self.logger.error(msg, extra=ex, stacklevel=2)

    def critical(self, msg, **kwargs):
        ex = {}
        for key, value in kwargs.items():
            ex[key] = value
        self.logger.critical(msg, extra=ex, stacklevel=2)


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['ts'] = datetime.datetime.fromtimestamp(record.created, datetime.timezone.utc).replace(
            tzinfo=None).isoformat(sep='T', timespec='milliseconds') + 'Z'
        log_record['level'] = record.levelname.lower()
        log_record['svc'] = record.name
        log_record['msg'] = log_record.pop('message')
        log_record['host'] = HOST
        log_record['func'] = record.module + '.' + record.funcName
        log_record['loc'] = record.filename + ':' + str(record.lineno)
