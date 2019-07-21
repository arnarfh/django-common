import os


def add_env_to_context(request):
    return {"env": os.getenv("ENV")}
