FROM python:latest

# Set working directoryn and 'cd' to it
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app
 ## cache dependencies ##
RUN pip install --no-cache-dir --upgrade -r requirements.txt 

# Copy script to folder
COPY . /app

# Start server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]