alias cp='cp'
wget --user=hassio --password='xj780224' ftp://localhost/share/wukongdata/config.yml
cp -f config.yml /root/.wukong/config.yml
python3 wukong.py
