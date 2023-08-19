FROM python:3-slim
WORKDIR /bot
COPY requirements.txt requirements.txt
RUN apt update -y && apt -y upgrade
RUN apt install -y ffmpeg
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .
CMD python3 -m bot