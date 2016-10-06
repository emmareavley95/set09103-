from flask import Flask, request, url_for
app = Flask(__name__)

@app.route("/")
def root():
  return "Hello Emma!"

@app.route("/display/")
def display():
  return '<img src="'+url_for('static', filename='uploads/file.png'
    )+'"/>'

@app.route("/upload/", methods=['POST','GET'])
def account():
  if request.method == 'POST':
    f = request.files['datafile']
    f.save('static/uploads/file.png')
    return "File Uploaded"
  else:
    page='''
    <html>
    <body>
    <form action="" method="post" name="form" enctype="multipart/form-data">
      <input type="file" name="datafile" />
      <input type="submit" name="submit" id="submit">
    </form>
    </body>
    </html>
    '''
    return page, 200

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
  return str(first+second)

@app.route('/static/img')
def static_img():
  start = '<img src="'
  url = url_for('static', filename='macaron.jpeg')
  end = '">'
  return start+url+end, 200

@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

