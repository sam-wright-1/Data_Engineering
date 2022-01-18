from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api, Resource
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
api = Api(app,
          version='10.5',
          title='Flask Restplus Demo',
          description='This is a trial',
          license='MIT',
          contact='Sam Wright',
          contact_url='https://www.linkedin.com/in/samuel-wright/',
          prefix='/test'
          )

upload_parser = api.parser()
upload_parser.add_argument('file', 
                           location='files',
                           type=FileStorage)

@api.route('/upload/')
@api.expect(upload_parser)
class UploadDemo(Resource):
    def post(self):
        args = upload_parser.parse_args()
        file = args.get('file')
        print(file.filename)
        return "Uploaded file is " + file.filename
    
if __name__ == '__main__':
    app.run()