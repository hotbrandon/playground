from pydantic import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_pass: str

# export environment variables before running this program
# export db_user='jennifer'
# export db_pass='123456'
# 如果 db_user, db_pass 未指定也沒有預設值，pydantic 會試著從環境變數取值
print(Settings().dict())

class Settings2(BaseSettings):
    my_secret:str

    class Config:
        env_file = '' # 可以吃 .env, 未指定檔名時會從目前路徑往上找
        env_file_encoding = 'utf-8'

print(Settings2().dict())