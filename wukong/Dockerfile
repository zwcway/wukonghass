LABEL io.hass.version="latest" io.hass.type="addon" io.hass.arch="armhf|aarch64|i386|amd64"
FROM wzpan/wukong-robot-arm:1.8.0
MAINTAINER wzpan
WORKDIR /root/wukong-robot
RUN git pull -f
RUN pip3 install -r requirements.txt
WORKDIR /root/.wukong/contrib
RUN git pull -f
RUN pip3 install -r requirements.txt
WORKDIR /root/wukong-robot
EXPOSE 5000
