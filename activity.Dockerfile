FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt amqp.reqs.txt ./
RUN python -m pip install --no-cache-dir -r http.reqs.txt -r amqp.reqs.txt
COPY ./activity.py ./invokes.py ./amqp_setup.py ./
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
CMD [ "python", "./activity.py" ]
=======
CMD [ "python", "./activty.py" ]
>>>>>>> Stashed changes
=======
CMD [ "python", "./activty.py" ]
>>>>>>> Stashed changes
=======
CMD [ "python", "./activty.py" ]
>>>>>>> Stashed changes
=======
CMD [ "python", "./activty.py" ]
>>>>>>> Stashed changes
