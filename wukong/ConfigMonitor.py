# -*- coding: utf-8-*-

import os
from robot import config, utils, logging
from watchdog.events import FileSystemEventHandler
from ftplib import FTP 
import os
import fileinput

logger = logging.getLogger(__name__)

def upload(f, remote_path, local_path):
    fp = open(local_path, "rb")
    buf_size = 1024
    f.storbinary("STOR {}".format(remote_path), fp, buf_size)
    fp.close()
                
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
                ftp.connect('192.168.1.229', 21) 
                ftp.login('hassio','xj780224')
                ftp.cwd('share/wukongdata')
                ftp.delete(config.yml)
                upload(ftp, "/root/.wukong/config.yml", "config.yml")
                logger.info("uploaded")
                config.reload()
                self._conversation.reInit()
