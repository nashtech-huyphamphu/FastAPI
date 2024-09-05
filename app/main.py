from fastapi import FastAPI
from routers import company, user
import sys
sys.path.append("C:/FastAPI")

app=FastAPI()

app.include_router(company.router)
app.include_router(user.router)

@app.get("/")
async def health_check():
    return "API service is up and running"