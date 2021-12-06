# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app, version='0.0.1', title='rentchairs API',
          description='You\'ll find all the public content calls',
          )

homes_ns = api.namespace(
    'v1/homes', description='Returns homes given specific parameters')

@homes_ns.route('/by-postal_code')
class HomesByPostalCode(Resource):
    @homes_ns.doc(params={
        'postal_code': 'Desired postal code',
    })
    def get(self, postal_code = None): 
        parameters = request.args
        return jsonify(
        [
            {
                'id': '1',
                'name': 'Casa Mar - Cala Montgó',
                'slug': 'casa-mar-cala-montgo',
                'lat': 42.110335912946624, 
                'lng': 3.159416807749598,
                'main_image_url': 'https://es.costabrava.org/files/fotos/100375_4644.jpg' 
            },
            {
                'id': '2',
                'name': 'Casa Cel - Cala Montgó',
                'slug': 'casa-cel-cala-montgo',
                'lat': 42.11022896057821, 
                'lng': 3.159536166054443,
                'main_image_url': 'https://redcostabrava.com/wp-content/uploads/2015/05/cala-montgo_02.jpg' 
            }
        ]
    )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8899, debug=True)

