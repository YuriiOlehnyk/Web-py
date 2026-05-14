FROM python:3.12-slim

WORKDIR /myproject

COPY requirements.txt .
# install dependencies without cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# gather static files in one folder
RUN python manage.py collectstatic --noinput

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "myproject.wsgi:application"]