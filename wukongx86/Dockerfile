FROM wzpan/wukong-robot:latest
MAINTAINER zwcway
ENV LANG C.UTF-8
WORKDIR /root/wukong-robot
RUN git pull -f && pip3 install -r requirements.txt && cd /root/.wukong/contrib && git pull -f && pip3 install -r requirements.txt && cp -f /root/wukong-robot/ConfigMonitor.py /root/wukong-robot/robot/ConfigMonitor.py && cp /root/wukong-robot/run.sh / && chmod a+x /run.sh
EXPOSE 5000
CMD [ "/run.sh" ]
