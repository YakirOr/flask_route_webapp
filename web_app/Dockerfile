
FROM python:3.8-slim

#Working directory
WORKDIR /flask_webapp

#Copy requirements file to container
COPY web_app/requirements.txt requirements.txt

#Install the dependencies
RUN pip install updates &&\
    pip install --upgrade pip  

RUN pip install -r requirements.txt

#Copy the flask appication code to the container
COPY web_app/flask_web_app.py flask_web_app.py

#Start the application
CMD ["python", "flask_web_app.py"]