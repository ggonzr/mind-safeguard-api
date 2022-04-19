from src.api import app
import uvicorn

# Application server
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3000, log_level='info')


