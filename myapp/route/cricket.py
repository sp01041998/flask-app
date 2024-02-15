from flask import Blueprint


cricket = Blueprint('cricket', __name__)

@cricket.route('/', methods=["GET"])
def testing():
    return "We are cricket playng countries"