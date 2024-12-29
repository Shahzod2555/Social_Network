from flask import Blueprint, send_from_directory

utils_blueprint = Blueprint('utils_blueprint', __name__)

@utils_blueprint.route('/media/<path:filename>')
def media_files(filename):
    return send_from_directory('./media', filename)
