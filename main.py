import uvicorn
from app import app
  
if __name__ == "__main__":
  config = uvicorn.Config(app, port= 5000, log_level= "info", reload= True)
  server = uvicorn.Server(config)
  server.run()