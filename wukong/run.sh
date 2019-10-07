alias cp='cp'
wget --user= --password='admin123' ftp://localhost/wukongdata/config.yml
cp -f config.yml /root/.wukong/config.yml
python3 wukong.py
