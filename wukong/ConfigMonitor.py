# -*- coding: utf-8-*-

import os
from robot import config, utils, logging
from watchdog.events import FileSystemEventHandler
from ftplib import FTP 
import os
import fileinput

logger = logging.getLogger(__name__)
ftp = FTP()

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
                config.reload()
                logger.info("uploading changed profile.")
                ftp.set_debuglevel(2)
                ftp.connect('192.168.1.229', 21) 
                ftp.login('hassio','xj780224')
                localfile="/root/.wukong/config.yml"
                ftp.cwd('/share/wukongdata')
                ftp.delete(config.yml)
                fp = open(localfile, 'rb')
                ftp.storbinary('STOR %s' % os.path.basename(localfile), fp, 1024)
                fp.close()
                logger.info("uploaded")
                self._conversation.reInit()
