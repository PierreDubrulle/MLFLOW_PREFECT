from fastapi import FastAPI, UploadFile, File
import json
import os

app = FastAPI()



@app.post("/uploadfile/")
async def post_data(file: UploadFile = File(...)):

    with open('./data.json', 'wb') as f:
        f.write(await file.read())
    



@app.get("/get_json")
async def share_data():
    if os.path.isfile('./data.json') is False:
        return f'Pas encore de data à récupérer...'
    with open('./data.json', "r") as f:
        data = json.load(f)
    return data

