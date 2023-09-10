FROM python:3.11.5-bookworm

WORKDIR /source

# Install Dependencies
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install psycopg2-binary=="2.9.7"

# Copy code
COPY ./code.py /source/code.py

CMD ["python", "/source/code.py"]