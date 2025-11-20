# Use the official Apify Python image
FROM apify/actor-python-playwright:3.11

# Copy the actor source code
COPY . ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium

# Specify the main entry point
CMD ["python", "-m", "src.main"]
