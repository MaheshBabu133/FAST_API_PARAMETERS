from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get('/Sample')
def sample(limit = 20,published:bool = False,sort : Optional[str] = None):
    if published:
        return {'data':f"{limit} limits",'status':"published",'sorted':sort}
    else:
        return {'data':f"{limit} limits",'status':"Not published",'sorted':sort}

#URL : http://127.0.0.1:8000/Sample?limit=300&published=true&sort=latest

@app.get('/Sample2/{id}')
def sample(id:int,limit = 20,published:bool = False,sort : Optional[str] = None):
    if published:
        return {'id':id,'data':f"{limit} limits",'status':"published",'sorted':sort}
    else:
        return {'id':id,'data':f"{limit} limits",'status':"Not published",'sorted':sort}

