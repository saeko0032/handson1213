import azure.functions as func
from data_ingestor import data_ingestor_bp
from indexer import indexer_bp

app = func.FunctionApp()

app.register_functions(indexer_bp)
app.register_functions(data_ingestor_bp)
