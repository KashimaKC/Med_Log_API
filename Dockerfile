From python:3

WORKDIR /api

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8080
CMD [ "python3", "main.py" ]
