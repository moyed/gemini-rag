FROM python:3.11

WORKDIR /app

# Copy and install dependencies
COPY requirement.txt /app
RUN pip install --no-cache-dir -r requirement.txt --default-timeout=100

# Copy the rest of your code
COPY . /app


EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]