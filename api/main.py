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
