import os

from project.settings.base import GA_CODE


def add_env_to_context(request):
    return {"env": os.getenv("ENV")}

def add_ga_code_to_context(request):
    return {"ga_code": GA_CODE}

def add_static_endpoint_to_context(request):
    end = None
    if os.getenv("ENV") == "production":
        from project.settings.production import AWS_STORAGE_BUCKET_NAME, DO_SPACE_ENDPOINT
        end = "https://" + AWS_STORAGE_BUCKET_NAME + "." + DO_SPACE_ENDPOINT + "/"
    if os.getenv("ENV") == "staging":
        from project.settings.staging import AWS_STORAGE_BUCKET_NAME, DO_SPACE_ENDPOINT
        end = "https://" + AWS_STORAGE_BUCKET_NAME + "." + DO_SPACE_ENDPOINT + "/"
    
    return {"static_files_public": end}