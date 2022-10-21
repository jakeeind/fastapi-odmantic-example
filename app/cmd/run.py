import uvicorn

def main():
    uvicorn.run("app.main:init_app", reload=True)