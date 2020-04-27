FROM python:alpine 

RUN mkdir -p /static
ADD . /static
WORKDIR /static
RUN pip3 install -r requirements.txt
CMD ["python3","run.py","dns"]  
