from pydantic import BaseModel

class ShipmentUpdate(BaseModel):
    receiver_name: str
    delivery_address: str

class ShipmentResponse(ShipmentUpdate):
    id: int
    tracking_code: str

    class Config:
        from_attributes = True