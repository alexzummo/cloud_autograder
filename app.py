from flask import Flask
from flask import jsonify, request
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

#class Data(db.Model):
#    """This is overkill, but it's just a demo anyway"""
#    __tablename__ = "Data"
#    id = db.Column(db.Integer, primary_key=True)
#    temp = db.Column(db.Integer)
#    setpoint = db.Column(db.Integer)
    
app = Flask(__name__)

def get_data():
    try:
        f = open("data.txt", "r")
    except FileNotFoundError:
        f = open("data.txt", "w")
        print("70", file=f)
        print("70", file=f)
        f.close()
        return [70, 70]
    temp = int(f.readline().strip())
    setpoint = int(f.readline().strip())
    f.close()
    return [temp, setpoint]

def write_data(setpoint):
    temp = get_data()[0]
    f = open("data.txt", "w")
    print(temp, file=f)
    print(setpoint, file=f)
    
@app.route("/")
def index():
    return "Welcome to thermostat"

@app.route("/ThermsAreUs/api/v1.0/current-temp", methods=["GET"])
def get_temp():
    # temp = Data.query.filter_by(id=0).first().temp
    temp = get_data()[0]
    return str(temp)

@app.route("/ThermsAreUs/api/v1.0/current-setpoint", methods=["GET", "PUT"])
def setpoint():
    # data = Data.query.filter_by(id=0).first()
    
    if request.method == "GET":
        setpoint = get_data()[1]
        return str(setpoint)
    elif request.method == "PUT":
        new_setpoint = request.form.get("setpoint")
        write_data(new_setpoint)
        # new_data = Data(id=0, temp=data.temp, setpoint=new_setpoint)
        # db.session.add(new_data)
        # db.session.commit()
        return str(new_setpoint)
    else:
        return jsonify({"success": False, "error": "Method not allowed"})


# if __name__ == '__main__':
app.run(debug=True, host="0.0.0.0")
