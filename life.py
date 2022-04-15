from fastapi import FastAPI, HTTPException

from typing import Optional, List

from pydantic import BaseModel

app = FastAPI(title='LIFE API', version='v1')

class life(BaseModel):

    voiture : str
    marque : str
    capacité : int 

store_life = [

]  

print(store_life)

# crud: create, read, uptade. delete

@app.get('/')
async def home():
    return {'hello: world'}



# c'est ce qui sert a voir tout les post "life" que nous avons fait 
@app.get('/lifes/', response_model=List[life])
async def get_lifes():
    return store_life



# ce qui est en bas sert a retrouver tout les post que j'ai fait grace a des [id] 
# imaginon je fait trois post je veux retrouver le premier je vais dans les docs 
# et je vais dans '[get] /life/{id}' et je met le numéro du post que je veux retrouver
# et si on a pas fait de post ce la va mettre 'Life not found in DB' --> c'est une erreur
@app.get('/life/{id}')
async def get_life(id: int):
    try:
        return store_life[id]
    except:
        raise HTTPException(status_code=404, detail='Life not found in DB')   



# cela sert a créer le post pour ensuite le retrouver dans /life/{id}
@app.post('/life')
async def create_life(life: life):
    store_life.append(life)
    return life




# ce qui sert a modifier un post pour le faire il faut mettre son id et ensuite nous pouvons 
# le modifier (après avoir fait un post biensur)
@app.put('/life/{id}')
async def uptade_life(id: int, new_life: life):
    try:
        store_life[id] = new_life
        return store_life[id]
    except:
        raise HTTPException(status_code=404, detail='Life not found in DB')



# delete cela sert a supprimer en mettant l'id au post que l'on veut supprimer 
@app.delete('/life/{id}')
async def delete_life(id: int):
    try:
        obj = store_life[id]
        store_life.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404, detail='Life not found in DB')   