FROM nginx:alpine
RUN apk update && apk add python3
RUN mkdir /static
ADD ../../ /static
WORKDIR /static
RUN pip3 install -r requirements.txt
CMD ["python3","run.py","nginx"]


