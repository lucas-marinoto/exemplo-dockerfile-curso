FROM python:alpine
COPY /app /app
RUN apk add py3-pip 
RUN pip3 install -r /app/requirements.txt
EXPOSE 5000
CMD [ "python3", "./app/app.py" ]