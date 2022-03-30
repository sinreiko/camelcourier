FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN python -m pip install -r http.reqs.txt
COPY ./rate.py ./
CMD [ "python", "./rate.py" ]
