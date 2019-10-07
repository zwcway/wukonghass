alias cp='cp'
wget --user=NAME --password='PASSWORD' ftp://localhost/wukongdata/config.yml
cp -f config.yml /root/.wukong/config.yml
python3 wukong.py
