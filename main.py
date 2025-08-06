from fastapi import FastAPI,HTTPException
from services import Services

app=FastAPI()

@app.get("/https://jsearch.p.rapidapi.com/search?query=developer%20jobs%20in%20chicago&page=1&num_pages=1&country=us&date_posted=all")
async def get_job_result():
    try:
        result=Services().get_job_result()
        return result
    except Exception as e:
        raise HTTPException(status_code=500,details="internal error")

@app.get("/https://jsearch.p.rapidapi.com/search?query=developer%20jobs%20in%20chicago&page=1&num_pages=1&country=us&date_posted=all")

async def get_job_search():
    try:
        result=Services().get_job_search()
        return result
    except Exception as e:
        raise HTTPException(status_code=500,details="internal error")

@app.get("/https://jsearch.p.rapidapi.com/estimated-salary?job_title=nodejs%20developer&location=new%20york&location_type=ANY&years_of_experience=ALL")
async def job_salary():
    try:
        result=Services().get_job_salary()
        return result
    except Exception as e:
        raise HTTPException(status_code=500,details="internal error")