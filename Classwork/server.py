import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/n", methods=["GET"])
def server_status():
    return "Server On"


@app.route("/info", methods=["GET"])
def info_route():
    return "This server was written for BME 547"


@app.route("/HDL_analysis", methods=["POST"])
def hdl_route_handler():
    """
    in_data = {"name": <patient_name>,
               "HDL_value": <HDL_result> }
    :return: string, HDL diagnosis
    """
    from blood_calculator import HDL_analysis
    in_data = request.get_json()
    print("Received HDL value of {}".format(in_data["HDL_value"]))
    diagnosis = HDL_analysis(in_data["HDL_value"])
    return jsonify(diagnosis)


@app.route("/add", methods=["POST"])
def add_numbers():
    """
    in_data = {"a": <first element>,
               "b": <second element> }
    :return:
    """
    in_data = request.get_json()
    summed = in_data["a"] + in_data["b"]
    if summed < 0:
        return "The answer was less than zero. BAD", 400
    return jsonify(summed)


@app.route("/add_two/<a>/<b>", methods=["GET"])
def add_two_numbers(a, b):
    """
    in_data = {"a": <first element>,
               "b": <second element> }
    :return:
    """
    summed = int(a) + int(b)
    return jsonify(summed)


if __name__ == '__main__':
    app.run()


