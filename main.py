import uvicorn as uvicorn

from core.config import config

if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=False if config.ENV == 'production' else True,
        workers=1,
        use_colors=True,
    )
