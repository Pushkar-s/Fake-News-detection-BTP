FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install python3.7 -y
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install pandas
RUN pip install numpy
RUN pip install scikit-learn
RUN pip install nltk
RUN pip install seaborn
RUN pip install tensorflow
RUN pip install Keras
RUN pip install -r requirements.txt
COPY . /app
ENV PORT=5000
EXPOSE 5000
CMD [ "python3", "./start.py" ]

