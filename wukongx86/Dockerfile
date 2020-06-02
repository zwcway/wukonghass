FROM wzpan/wukong-robot:latest
MAINTAINER zwcway
ENV LANG C.UTF-8
WORKDIR /root/wukong-robot
RUN git pull -f && pip3 install -r /root/wukong-robot/requirements.txt && cd /root/.wukong/contrib && git pull -f && pip3 install -r /root/.wukong/contrib/requirements.txt && cp -f ConfigMonitor.py /root/wukong-robot/robot/ConfigMonitor.py && cp -f run.sh / && chmod a+x /run.sh
EXPOSE 5000
CMD [ "/run.sh" ]
