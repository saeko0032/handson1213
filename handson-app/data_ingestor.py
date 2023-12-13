import azure.functions as func
import logging

data_ingestor_bp = func.Blueprint()


@data_ingestor_bp.function_name(name="data-upload")
@data_ingestor_bp.route(route="data/upload_json", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def data_loader(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Function(data/upload_json) processed .')

    return func.HttpResponse('{"value": "Hello from data loader"}',
                             mimetype="application/json",
                             status_code=200)
