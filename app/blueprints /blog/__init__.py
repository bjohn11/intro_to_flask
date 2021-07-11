from . import routes
from flask import Blueprint


bp = Blueprint('blog', __name__, url_prefix='/blog')

#. means from whatever folder we are in
