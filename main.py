from fastapi import FastAPI
from typing import Optional  # 옵셔널 파라미터 


app = FastAPI()

"""
@app.get("/countries/korea") # 맨 처음 루트 페이지에 액서스가 있으면 밑에 함수가 실행 ,, path operation
# {안에}  path parameter 
async def korea() :   # 비동기 처리 ,, type hints로 머가 들어올지 제한 가능  
    return {"message" : "This is Korea"} 



@app.get("/countries/{country_name}") # 맨 처음 루트 페이지에 액서스가 있으면 밑에 함수가 실행 ,, path operation
# {안에}  path parameter 
async def country(country_name: str) :   # 비동기 처리 ,, type hints로 머가 들어올지 제한 가능  
    return {"country_name" : country_name} 

"""


"""
# 쿼리 파라미터 
@app.get("/countries") 
async def country(country_name: str = 'korea', city_name: str = "Seoul") :  
    return {
        
        "country_name" : country_name,
        "city_name": city_name
        
        } 
# http://127.0.0.1:8000/countries/?country_name=America&city_name=Seoul 이러면 country_name : America, city_name : Seoul 이렇게 뜸 

@app.get("/countries/{country_name}") 
async def country(country_name: str = 'korea', city_name: str = "Seoul") :  
    return {
        
        "country_name" : country_name,
        "city_name": city_name
        
        } 
# http://127.0.0.1:8000/countries/america?city_name=newYork

"""


# 옵셔널 파라미터 
@app.get("/countries/{country_name}")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {

        "country_name": country_name,
        "country_no": country_no
    }


