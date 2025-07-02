FROM python:3.10-slim

# Install system dependencies
RUN apt update && apt install -y build-essential libffi-dev git

# Upgrade pip and install Qiskit and dependencies
RUN pip install --upgrade pip && \
    pip install qiskit==1.0.2 qiskit-aer==0.13.3 qiskit-algorithms==0.3.1 qiskit-optimization==0.6.0 \
                numpy==1.24.4 scipy==1.10.1 matplotlib

# Set working directory inside container
WORKDIR /app

# Copy current project files into container
COPY . .

# Set default command to run your main script
CMD ["python", "qubo_qaoa.py"]
