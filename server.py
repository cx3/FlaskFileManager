from app_routes import app, socketio
from auth_blueprint import bp, login_required

app.register_blueprint(bp, url_prefix='/auth')

for rule in app.url_map.iter_rules():
    print('Rule:', rule, '\t\tdecorated endpoint:', rule.endpoint)
    if rule.endpoint != 'static' and not rule.endpoint.startswith('auth'):
        view_func = app.view_functions[rule.endpoint]
        app.view_functions[rule.endpoint] = login_required(view_func)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
