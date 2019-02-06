import re
import datetime
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
   def get(self,uid):
      res = { "mensagem": "Bem vindo(a) {0}".format(uid) }
      return jsonify(res)

class Senha(Resource):
   def get(self):
      return "Funcionou a senha!"

   def post(self):
      #senha = request.form['senha']
      json_data = request.get_json(force=True)
      print json_data["senha"]
      return '',204

class Token(Resource):
   def get(self):
      return "Funcionou o token!"

   def post(self):
       request.form['token_jit']

api.add_resource(Pessoa, '/pessoas/<uid>')
api.add_resource(Senha, '/senhas')
api.add_resource(Token, '/tokens')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080,debug=True)
