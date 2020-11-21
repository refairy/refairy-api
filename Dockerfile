FROM python:3.8
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=refairy_api/app.py

CMD ["/usr/local/bin/flask", "run", "-h", "0.0.0.0"]
