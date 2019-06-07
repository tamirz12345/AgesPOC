from AgesMongo import AgesMongo
from flask import Flask, request, jsonify


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    ages = AgesMongo()
    

    @app.route('/info',methods=['GET'])
    def get_info():
        requested_username = request.args['username']
        return "Age is {age}".format(age=ages.get_age(requested_username))

    @app.route('/insert', methods=['GET'])
    def put_info():
        username = request.args['username']
        age = request.args['age']
        ages.insert_age(username,age)
        return jsonify(success=True)

    return app




def main():
    app = create_app()
    app.run()

if __name__ == "__main__":
    main()