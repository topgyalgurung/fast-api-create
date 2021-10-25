from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI();

# define JSON data models(data shape) or schema
# declare data model as class inherit frm BaseModel
class Item(BaseModel):
    name:str
    description:Optional[str]=None # 
    price:float
    tax:Optional[float]=None

""" app.get """

# order matters! fixed path first
@app.get("/") #root endpoint
async def read_root():
    return{"Hello":"Fast api learner"}

# get item by id with its type
@app.get("/items/curr_item")
async def read_cur_item():
    return{"cur_item":"the current item"}

@app.get("/items/{item_id}")
async def read_item(item_id:int, q:Optional[str]=None):
    return {"item_id":item_id,"q":q}

"""
# third party library call await 
#   result = await som_lib()
@app.get("/")
async def read_result():
    result= await some_lib()
    return result

# if 3rd p lib communicates with db, api or filesystem, no support for await
# then normal def
@app.get('/normal')
def results():
    results=some_lib()
    return results
"""

""" @app.post """
# add pydantic model to path as parameter
# with pydantic it supports autocompletion, error check for incorrect type
# for pycharm user, use pydantic pycharm plugin 
# i have pylance in vscode 
@app.post("/items")
async def create_item(item:Item):
    # access attr of model obj
    item_dict=item.dict()
    if item.tax:
        price_with_tax=item.price+item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

""" app.put """
@app.put("/items/{item_id")
async def create_item(item_id:int,item:Item):
    return {"item_id":item_id, **item.dict()}

# fastapi gives both data parsing & validation
# data handling or validation with pydantic 

# request body - data sent by client -> api ; use pydantic models
# response body: data sent by api -> client