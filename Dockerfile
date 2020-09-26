FROM python:3


RUN apt-get update
RUN pip3 install --upgrade pip
RUN mkdir /app
COPY  requirements.txt /app/requirements.txt
COPY ./ ./app
WORKDIR /app
RUN  pip3 install -r requirements.txt
EXPOSE 5000
VOLUME [ "/fetch/output/output_hamiltonwatch.csv" ]
CMD ["python3", "main.py"]