from flask import Blueprint, render_template
import os
import re 

from ..constants import FLASK_PROJECT_ROOT

frontend = Blueprint('frontend', __name__)

@frontend.route('/notebooks', methods=['GET'])
def notebook_index():
    """
    Show a list of notebooks
    """
    
    # get the html files from the templates
    jupyter_notebooks = os.listdir(os.path.join(FLASK_PROJECT_ROOT, 'templates', 'jupyter_notebooks'))
    html_files = [i for i in jupyter_notebooks if i.endswith('.html')]
    html_file_roots = [os.path.splitext(i)[0] for i in html_files]
    
    # render the templates
    return render_template('jupyter_notebooks.html', notebooks=html_file_roots)

@frontend.route('/notebooks/<notebook_name>', methods=['GET'])
def jupyter_notebook(notebook_name):
    return render_template("jupyter_notebooks/{}.html".format(notebook_name))