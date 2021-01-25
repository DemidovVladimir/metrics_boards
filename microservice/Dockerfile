FROM python:3.7
RUN mkdir /usr/src/api/
COPY . /usr/src/api/
WORKDIR /usr/src/api/
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "main.py"]