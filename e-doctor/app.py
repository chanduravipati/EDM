from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import json

app = FastAPI()

# Load Disease Symptoms Dataset
def load_diseases():
    diseases = []
    with open("diseases_symptoms.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            diseases.append(row)
    return diseases

diseases_data = load_diseases()

# Load Medicine Recommendations Dataset
def load_medicines():
    medicines = {}
    with open("disease_medicines.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            medicines[row["Disease"].lower()] = {
                "medicines": row["Medicines"].split(","),
                "dosage": row["Dosage"],
                "side_effects": row["Side Effects"],
            }
    return medicines

medicines_data = load_medicines()

# Models
class DiagnosisRequest(BaseModel):
    symptoms: str

class MedicineRequest(BaseModel):
    disease: str

class ConsultationRequest(BaseModel):
    firstName: str
    contactNumber: str
    village: str
    email: str
    issue: str

# Endpoints
@app.post("/diagnose")
def diagnose(request: DiagnosisRequest):
    symptoms = request.symptoms.lower().split(", ")
    likely_diseases = [
        disease["Disease"] for disease in diseases_data
        if all(symptom in disease["Symptoms"].lower() for symptom in symptoms)
    ]
    if not likely_diseases:
        raise HTTPException(status_code=404, detail="No matching diseases found.")
    return {"likely_diseases": likely_diseases}

@app.post("/recommend")
def recommend(request: MedicineRequest):
    disease = request.disease.lower()
    if disease not in medicines_data:
        raise HTTPException(status_code=404, detail="No medicine recommendations found.")
    return medicines_data[disease]

@app.post("/consultation")
def consultation(request: ConsultationRequest):
    with open("consultation_records.json", mode="r") as file:
        records = json.load(file)
    records.append(request.dict())
    with open("consultation_records.json", mode="w") as file:
        json.dump(records, file, indent=4)
    return {"message": "Consultation data saved successfully."}
