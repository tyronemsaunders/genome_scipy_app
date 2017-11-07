from flask import Blueprint
import os

from ..response import Response


health = Blueprint('health', __name__)

@health.route('/health', methods=['GET'])
def health_check():
    """
    Run a health check and return OK if server is running
    """
    return Response.make_success_resp(msg="OK")


