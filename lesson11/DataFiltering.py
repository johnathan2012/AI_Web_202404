import json
from pprint import pprint
from pydantic import BaseModel,Field,field_validator

class Records(BaseModel):
    公司名稱:str = Field(alias='Name_Ins')
    登記編號:str = Field(alias='No')
    地址:str = Field(alias='Address')
    統編:str = Field(alias='tax_ID_number')
    緯度:float = Field(alias='wgs84aX')
    經度:float = Field(alias='wgs84aY')

    @field_validator("緯度","經度",mode='before')
    @classmethod
    def abs(cls,value):
        if value == '':
            return 0.0
        else:
            return value


class Result(BaseModel):
    records:list[Records]   

with open('新北市食品工廠清冊.json',encoding='utf-8') as file:
    json_content:str = file.read()
    all_data = json.loads(json_content)
    #pprint(all_data)

result:Result = Result.model_validate(all_data['result'])

for rec in result.records:
    print(rec)