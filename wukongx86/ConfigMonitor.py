# -*- coding: utf-8-*-

import os
from robot import config, utils, logging
from watchdog.events import FileSystemEventHandler
import ftplib
from ftplib import FTP 
import fileinput

logger = logging.getLogger(__name__)

                
class ConfigMonitor(FileSystemEventHandler):
    def __init__(self, conversation):
        FileSystemEventHandler.__init__(self)
        self._conversation = conversation

    # 文件修改
    def on_modified(self, event):
        if event.is_directory:
            return

        filename = event.src_path
        extension = os.path.splitext(filename)[-1].lower()
        if extension in ('.yaml', '.yml'):
            if utils.validyaml(filename):
                logger.info("检测到文件 {} 发生变更".format(filename))
                logger.info("uploading changed profile.")
                ftp = FTP()
                ftp.set_debuglevel(2)
                ftp.connect('127.0.0.1', 21) 
                ftp.login('hassio','wukong2019hassio')
                ftp.cwd('share/wukongdata')
                ftp.delete("config.yml")
                os.chdir("/root/.wukong")
                file = open('config.yml', "rb")
                ftp.storbinary('STOR ' + 'config.yml', file)
                file.close() 
                ftp.quit() 
                logger.info("uploaded")
                config.reload()
                self._conversation.reInit()
