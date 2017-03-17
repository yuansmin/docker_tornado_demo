FROM daocloud.io/python:2.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/
ENTRYPOInT ["python"]
CMD ["app.py"]
