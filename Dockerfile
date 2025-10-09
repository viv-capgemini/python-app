FROM python:3.12.3-alpine

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY src /src/ 

EXPOSE 5000

CMD python /src/app.py