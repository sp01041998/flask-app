from flask import Blueprint

football = Blueprint('football', __name__)

@football.route('/', methods=["GET"])
def testing():
    return "We are footballing countries list"