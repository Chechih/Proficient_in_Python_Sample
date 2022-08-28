from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='.')

@route('/each/<thing>')
def each(thing):
    return 'Say hello to my little friend: %s!' % thing

run(host='localhost', port=9999)
