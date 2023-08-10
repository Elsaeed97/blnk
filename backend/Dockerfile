FROM python:3.11-alpine

# PREVENT PYTHON FROM WRITING BYTE CODE .pyc
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1


RUN apk update \
    && apk add --no-cache gcc musl-dev python3-dev postgresql-dev

# working directory
WORKDIR /app


COPY . /app/

# Install Python requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the Django development server port
EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
