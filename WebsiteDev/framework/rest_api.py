#By Sanjay-B(Sanjay Bhadra)
#Copyright SAGE. All Rights Reserved

#Routed through http://www.sage,io/api/

#To do:
# -- Documentation during July 2017[ ]
# -- Send mulipart/json tables[ ]
# -- Cache JSON objects from other APIs[ ]
# -- GET, POST[ ]
# -- Endpoints with data attached[ ]
# -- Making this valid through Client-Id or Token[ ]
# -- RateLimits to prevent overflow to servers[ ]



#REST WebSocket API for external applications
from flask import Flask
from flask_restful import Resource, Api

instance = Flask(__name__)
rest_api = Api(instance)

class Search_Thread(Resource):
    def get(self):
        return {'type':'GET','value':'nil'}


#Valid Request-API URLs
rest_api.add_resource(Search_Thread, '/api/search_thread')

if __name__ == '__main__':
    instance.run()
