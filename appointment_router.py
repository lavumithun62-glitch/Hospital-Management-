from fastapi import APIRouter

router = APIRouter(prefix="/appointments")

@router.get("/")
def get_appointments():
    return {"message": "Appointments API Working"}
