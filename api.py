from typing import Optional

from fastapi import FastAPI, Form

import uvicorn

from typing import Optional

from pydantic import BaseModel

app = FastAPI()

#class CoordIn(BaseModel):
#    password : str
#    freres : float
#    soeurs : float
#    parents : Optional[int] = None
#    description : Optional[str] = None

#class CoordOut(BaseModel):
#    freres : float
#    soeurs : float
#    parents : Optional[int] = None 
#    description : Optional[str]  = None                         # avec Optional je le rend optionelle  donc ce n'est pas obliger de le mettre



#@app.post('/position/', response_model=CoordOut, response_model_include={'description'})
#async def make_position( coord: CoordIn):
    # supposer que db write a été fait
#    return coord

@app.get("/")
async def hello_world():
    return{'hello' : 'world'}

#@app.post('/position/', response_model=CoordOut, response_model_exclude={'description'})
# si on met response_model_exclude et quelque chose de-dans cela veut dire
# que ca va retirer ce qui qui est de-dans comme sa "response_model_exclude{'voiture'}"
# cela va retirer voiture du post -->(du docs) --> http://127.0.0.1:8000/docs )

#@app.post('/position/', response_model=CoordOut, response_model_include={'description'})
# si on met response_model_include et quelque chose de-dans cela veut dire
# que ca va retirer tout ce qui qui est dans le post sauf {'description'}
# cela va retirer tout sauf desciption du post -->(du docs) --> http://127.0.0.1:8000/docs )

# @app.post('/position/{priority}')
# et on est obliger de le mettre dans le post
# il faut aussi le mettre dans notre return 
# return{'max': max, 'fammily': coord.dict(), 'value': value}<---- exemple
# on peut aussi mettre value comme en haut





#################post#############################################                                   
#class Coord(BaseModel):
    frère : int
    soeurs : int
    parents : Optional[int]

#@app.get("/")
#async def hello_world():
    return{'hello' : 'world'}

#@app.post('/famille/{priority}')
#async def make_famille(priority:int ,coord: Coord, value: bool):
    return {'priority': priority,'famille':coord.dict(), 'reponse': value}
################################################################################












@app.get('/voiture/{voiture_id}') #path parameter
async def get_voiture(voiture_id: int):
    # opérations
    return {'voiture' : voiture_id}

#@app.post('/login/')
#async def login(username: str, password: str):   # autre façon d'uttiliser path parameter
    return {username: password}                  # au dessus # plus facilement # c'est un post

#@app.get('/voiture/')
#async def read_voiture(number: int, text: Optional[str]):
    return{'number' : number, 'text' : text}

#http://127.0.0.1:8000/voiture/?number=12&text=voiture : 
# "number" : 12
# "text" : "voiture" ----> avec Optional[str]


# sans Optional :
# ->  "number" : 12
#     "text" : voiture
# ou
#     "number" : 
#     "text" :      -> si on écrit rien sur la barre d'adresse


#http://127.0.0.1:8000/voiture/?number=12&text= : 
# "number" : 12
# "text" : ""


#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=8000)

