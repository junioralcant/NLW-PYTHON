
from src.errors.errors_types.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.views.http_types.http_response import HttpResponse


def error_handle(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code, 
            body={
                "erros": [{
                    "title": error.name,
                    "details": error.message
                }] 
            }
        )
    
    return HttpResponse(
        status_code=500, 
        body={
            "erros": [{
                "title": "Server Error",
                "details": str(error)
            }] 
        }
    )
