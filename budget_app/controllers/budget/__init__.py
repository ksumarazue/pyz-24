from flask import Blueprint

budget_bp = Blueprint('budget', __name__, url_prefix='/budget')

from .views import *