FROM python:3.7.3-slim

RUN apt-get update && apt-get install -y wget && apt-get install -y unzip

# chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && wget https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip

# chromedriver
RUN wget https://moji.or.jp/wp-content/ipafont/IPAexfont/IPAexfont00401.zip \
    && unzip IPAexfont00401.zip -d ~/.fonts/ \
    && rm IPAexfont00401.zip

# 日本語フォントをダウンロード
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*