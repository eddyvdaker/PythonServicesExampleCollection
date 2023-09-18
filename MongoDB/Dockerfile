FROM python:3.11.5-bookworm

WORKDIR /source

# Install Dependencies
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install pymongo=="4.5.0"

# Copy code
COPY ./code.py /source/code.py

CMD ["python", "/source/code.py"]