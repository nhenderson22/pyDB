import typer
from database import DataBase

app = typer.Typer()

@app.command()
def get(path:str,key:str):
    db = DataBase(path)
    print(db.getTable(key))
@app.command()
def create(path:str,key:str,info:str):
    db = DataBase(path)
    db.createTable(key,info)
    db.write()

if __name__ == "__main__":
    app()

