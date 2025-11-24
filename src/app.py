from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.database import SessionLocal, get_db
from src.models import News, Entity
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Получение графа сущностей с привязанными к ним новостями


@app.get("/graph")
def get_graph(db: Session = Depends(get_db)):
    entities = db.query(Entity).all()
    graph_data = []

    for entity in entities:
        news_list = [{"id": news.id, "text": news.text, "link": news.link} for news in entity.news]
        graph_data.append({
            "id": entity.id,
            "name": entity.name,
            "type": entity.type,
            "news": news_list
        })

    return {"nodes": graph_data}
