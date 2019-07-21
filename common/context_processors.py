import os

from project.settings.base import GA_CODE


def add_env_to_context(request):
    return {"env": os.getenv("ENV")}

def add_ga_code_to_context(request):
    return {"ga_code": GA_CODE}