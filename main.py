import uvicorn

from fastapi import FastAPI

from routers import stable_diffusion


def initialize_stable_diffusion():
    import sys
    sys.path.append('stable-diffusion-webui')
    from importlib import import_module
    import_module("modules.paths")
    import_module("modules.sd_samplers")
    import_module("webui").initialize()


if __name__ == "__main__":
    initialize_stable_diffusion()

    app = FastAPI()
    app.include_router(stable_diffusion.router)
    uvicorn.run(app, host="127.0.0.1", port=8000)
