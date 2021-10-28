FROM python:3.8-slim-buster
WORKDIR /app

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    python3-opencv \
    ffmpeg \
    libsm6 \
    libxext6 \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/factory.py src/factory.py
RUN python src/factory.py

COPY . .
RUN pip install .

CMD ["streamlit", "run", "src/webapp.py"]