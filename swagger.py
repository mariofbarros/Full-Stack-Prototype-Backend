# swagger.py
import os
import yaml
from flasgger import Swagger
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def init_swagger(app, spec_file='swagger.yaml'):
    #Initialize Flasgger with an external OpenAPI spec file.
    
    spec_path = os.path.join(BASE_DIR, spec_file)
    
    with open(spec_path, 'r') as f:
        swagger_config = yaml.safe_load(f)
    
    swagger = Swagger(app, template=swagger_config, template_file=None)
    
    return swagger