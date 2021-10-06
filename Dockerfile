FROM python:3
COPY . .
CMD ["webserver.py"]
ENTRYPOINT ["python3"]