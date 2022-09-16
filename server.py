from fastapi import FastAPI
import uvicorn
import os
from request import Request_DTO
from summary import summarize as summary


app = FastAPI()
PER = float(os.environ.get('PER',0.5)) 


@app.get('/ping')
def ping():
    return 'up and running'

@app.post('/summarize')
def summarize(req: Request_DTO):
    res = summary(req.text,PER)
    return {'summary':res}


if __name__ == '__main__':
    uvicorn.run(app ,host='0.0.0.0',port=os.environ.get('PORT',8080))
    