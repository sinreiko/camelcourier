FROM python:3-slim
WORKDIR /usr/src/app
RUN pip install Flask twilio
COPY ./send_sms.py .
CMD [ "python", "./send_sms.py" ]