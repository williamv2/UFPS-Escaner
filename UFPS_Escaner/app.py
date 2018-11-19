from flask import Flask, render_template
from string import digits, ascii_lowercase
from random import sample
from UFPS_Escaner.views.authenticate import login_check, authenticate
from UFPS_Escaner.views.index import index
from UFPS_Escaner.views.vul_scanner import vul_scanner
from UFPS_Escaner.views.asset_management import asset_management
from UFPS_Escaner.views.plugin_management import plugin_management
from UFPS_Escaner.views.settings import settings
from UFPS_Escaner.views.dashboard import dashboard
from UFPS_Escaner.views.port_scanner import port_scanner
from UFPS_Escaner.views.subdomain_brute import subdomain_brute
from UFPS_Escaner.views.acunetix_scanner import acunetix_scanner
from UFPS_Escaner.views.auth_tester import auth_tester


app = Flask(__name__)
app.config['SECRET_KEY'] = ''.join(sample(digits + ascii_lowercase, 10))

app.register_blueprint(authenticate)
app.register_blueprint(index)
app.register_blueprint(vul_scanner)
app.register_blueprint(asset_management)
app.register_blueprint(plugin_management)
app.register_blueprint(settings)
app.register_blueprint(dashboard)
app.register_blueprint(port_scanner)
app.register_blueprint(subdomain_brute)
app.register_blueprint(acunetix_scanner)
app.register_blueprint(auth_tester)


@app.errorhandler(404)
@login_check
def page_not_fount(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
@login_check
def internal_server_error(e):
    return render_template('500.html'), 500
