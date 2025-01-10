from fastapi import FastAPI
from pydantic import BaseModel

class RandomFact(BaseModel):
    id: int
    fact: str
    
app=FastAPI()

RandomFactGenerator=[RandomFact(id=1,fact='A group of flamingos is called a flamboyance'),RandomFact(id=2,fact='There are more stars in the universe than grains of sand on Earth')]

# GET
@app.get('/fact/')
async def get_facts():
    return RandomFactGenerator
@app.get('/fact/{id}')
async def get_id(id):
    return (i for i in RandomFactGenerator if i.id == int(id))

# POST
@app.post('/fact/')
async def add_new_fact(NewRandomFact: RandomFact):
    RandomFactGenerator.append(NewRandomFact)
    return NewRandomFact

#PUT
@app.put('/fact/{id}')
async def update_facts(updatedRandomFact: RandomFact, id):
    for RandomFact in RandomFactGenerator:
        if RandomFact.id == int(id):
            RandomFact=updatedRandomFact
            return RandomFact
        return None

#DELETE
@app.delete('/fact/{id}')
async def delete_facts(id):
     for f in RandomFactGenerator:
       if f.id == int(id):
           RandomFactGenerator.remove(f)
     return None
    