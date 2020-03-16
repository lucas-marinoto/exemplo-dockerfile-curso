FROM python:alpine
COPY /app /app
RUN apk add py3-pip 
RUN pip3 install -r /app/requirements.txt
CMD [ "python3", "./app/app.py" ]