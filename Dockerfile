# Use the optimized FastAPI image
FROM tiangolo/uvicorn-gunicorn:python3.10 AS fastapi-backend-base

# Upgrade pip
RUN pip install --upgrade pip

# Create working directory
RUN mkdir /fastapi-backend
WORKDIR /fastapi-backend

# Copy and install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy project files
COPY . ./

# Expose the correct port
EXPOSE 8000

# Run FastAPI with specified settings
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "error", "--lifespan", "on"]
