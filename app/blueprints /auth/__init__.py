from flask import Blueprint


bp = Blueprint('auth', __name__, url_prefix='/auth')

#. means from whatever folder we are in
from . import routes