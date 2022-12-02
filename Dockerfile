FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt -y update && apt -y upgrade
RUN apt install -y git curl apt build-essential portaudio19-dev libsndfile1

# Install python 3.8
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y python3.8
RUN apt install -y python3.8-distutils
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 20
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN apt install -y python3.8-dev
COPY requirements.txt /
RUN pip install -r requirements.txt

RUN apt install -y ffmpeg
COPY . /xiangqi-ai
WORKDIR /xiangqi-ai

CMD python main.py