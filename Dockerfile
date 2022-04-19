FROM python:3.10.4-slim-buster
LABEL author="Geovanny Gonzalez-Rodriguez"
LABEL github="ggonzr"
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3000
CMD [ "python", "main.py" ]
