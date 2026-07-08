# Step 1: Use an official, lightweight Python base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy only the requirements file first to take advantage of Docker layer caching
COPY requirements.txt .

# Step 4: Install all framework dependencies directly inside the image
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your automation framework code into the container
COPY . .

# Step 6: Define the default command to run when the container executes
# We use 'pytest' because our new pytest.ini handles all default arguments!
CMD ["pytest"]