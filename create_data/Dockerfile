
FROM python:3.9-slim-buster

#RUN apt-get update && apt-get -y install cron


COPY . .

RUN pip install -r requirements.txt
#COPY crontab /etc/cron.d/crontab


#RUN chmod 0644  /etc/cron.d/crontab
#RUN chmod 0644  ./app.py
#RUN /usr/bin/crontab etc/cron.d/crontab

CMD ["python", "app.py"]