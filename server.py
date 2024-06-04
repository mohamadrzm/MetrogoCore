from fastapi import FastAPI
from pydantic import BaseModel
from libs.lib import check_match_name, find_best_path

class RouteData(BaseModel):
    source: str
    destination: str
    color: bool = False

app = FastAPI()

@app.post("/v1/get_route")
async def get_route(route_data: RouteData):
    source = check_match_name(route_data.source)
    destination = check_match_name(route_data.destination)

    if not source:
        return 'Source not found!'
    if not destination:
        return 'Destination not found!'

    return find_best_path(source=source, dist=destination, color=route_data.color)
