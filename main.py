from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s- api - %(asctime)s - %(message)s')
api_logger = logging.getLogger("api server")
api_logger.setLevel(logging.DEBUG)


app = FastAPI(title="Eric's Minecraft servertap webhook",
              description="To provide webhook endpoints for minecraft",
              version="0.1")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/debug')
async def debug(info: dict):
    """Print out what is sent to the endpoint for debugging purposes."""
    api_logger.debug(info)
