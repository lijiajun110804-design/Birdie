# from fastapi import FastAPI
# from fastapi import FastAPI
# from app.database import Base, engine
# from app.models import User
# from fastapi import FastAPI
# from app.database import Base, engine
# from app.models import User
# from app.routers import test_user

# app = FastAPI(title="Birdie Backend API")

# @app.get("/health")
# def Health_Check():
#     return{"status": "ok"}

# app = FastAPI()

# Base.metadata.create_all(bind=engine)


# @app.get("/health")
# def health():
#     return {"status": "ok"}、


# app = FastAPI()

# Base.metadata.create_all(bind=engine)

# app.include_router(test_user.router)


# @app.get("/health")
# def health():
#     return {"status": "ok"}

from fastapi import FastAPI

from app.database import Base, engine
from app.models import User
from app.routers import test_user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Birdie Backend API")

app.include_router(test_user.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}