# 1. Start from an image that already has Python installed

FROM python:3.11.4-slim

# 2. Create and move into a folder inside the container
WORKDIR /app

# 3. Copy only requirements first (enables layer caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code
COPY . .

# 6. Document the port the app uses
EXPOSE 8000

# 7. Command that runs when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]