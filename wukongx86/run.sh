alias cp='cp'
wget --user=hassio --password='wukong2019hassio' ftp://127.0.0.1/share/wukongdata/config.yml
wget --user=hassio --password='wukong2019hassio' ftp://127.0.0.1/share/wukongdata/wukong.pmdl
cp -f config.yml /root/.wukong/config.yml
cp -f wukong.pmdl /root/.wukong/wukong.pmdl
python3 wukong.py
