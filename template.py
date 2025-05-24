import os

# Define the main project directory
project_root = "Flight_Price_Prediction"

# Define subdirectories to create
subdirs = ["app", "api", "models", "data"]

# Define template files and contents
file_templates = {
    "app/__init__.py": "",
    "app/data_loader.py": "# Functions to load and preprocess flight data\n",
    "app/feature_engineering.py": "# Functions for feature extraction from flight data\n",
    "app/model.py": "# Model training, saving, and loading logic\n",
    "app/predictor.py": "# Use trained model to make predictions\n",
    "api/main.py": """\
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FlightData(BaseModel):
    Airline: str
    Date_of_Journey: str
    Dep_Time: str
    Arrival_Time: str
    Source: str
    Destination: str
    Route: str
    Duration: str
    Total_Stops: str
    Additional_Info: str

@app.post("/predict")
def predict_flight_price(data: FlightData):
    return {"fare": "Prediction will appear here"}
""",
    "Dockerfile": """\
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
""",
    "requirements.txt": "fastapi\nuvicorn\npandas\nscikit-learn\njoblib\nopenpyxl\n",
    "README.md": "# Flight Price Prediction Project\n"
}

# Create root directory
os.makedirs(project_root, exist_ok=True)

# Create subdirectories
for subdir in subdirs:
    os.makedirs(os.path.join(project_root, subdir), exist_ok=True)

# Create template files
for file_path, content in file_templates.items():
    full_path = os.path.join(project_root, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Project structure created in '{project_root}/'")
