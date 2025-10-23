from fastapi  import FastAPI,Path
from typing import Annotated

app= FastAPI()

cursos=[
  "digital solutions",
  "Mecatronica"
  "manufatura eletronica",
  "manufatuta digital",
  "manufatura Automativa",
  "Adminstração"
  
  ]

instrutores=[
  "Cleber Angusto",
  "Francis Franquini",
  "Menininho da VoVo",
  "Leonardo Oliveiro",
  "Paulo Oliveira",
  "Vanessa Silva"
  ]


@app.get("/cursos")
async def root():
  return {"cursos" :cursos}

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id:Annotated[int,Path(title = "o id do curso da ETS",  ge=0, lt=6)]):
  
  # curso_id= int(cursos_id)
  return{"cursos": cursos[curso_id]}

@app.get('/instrutores')
async def get_instrutores(pos_inicial: int=0, pos_final: int=7):

     return {"instrutores": instrutores[pos_inicial: pos_final]}

    
