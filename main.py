from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
import models
import schemas
import user_service

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.put("/shipments/{shipment_id}", response_model=schemas.ShipmentResponse)
def update_shipment(
    shipment_id: int, 
    shipment_data: schemas.ShipmentUpdate, 
    db: Session = Depends(get_db)
):
    return user_service.update_shipment_service(
        db=db, 
        shipment_id=shipment_id, 
        shipment_update=shipment_data
    )