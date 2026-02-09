from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {"message":"Fuck! this shit is working. Cool!"}

