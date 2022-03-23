FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN pip install -r http.reqs.txt
COPY ./user_auth.py ./
CMD [ "python", "./user_auth.py" ]