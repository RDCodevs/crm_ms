import uvicorn
from src.app import app
  
if __name__ == "__main__":
  config = uvicorn.Config(app, port= 5000, reload= True, log_level= "info")
  server = uvicorn.Server(config)
  uvicorn.run(server)