from flask import Flask, request, jsonify, render_template
from utils import Predict_CO2_Emission
import config

app = Flask(__name__)

@app.route('/')

def home():
    #return jsonify({"Result":"success"})
    return render_template('co2_emmission1.html')


@app.route('/co2_emmission', methods = ['GET','POST'])
def predict_co2():
    if request.method=='GET':

        data = request.args.get
        print('data : ',data)
        make = data('make')
        model = data('model')
        Vehicle_Class = data('Vehicle_Class')
        Engine_Size=eval(data('Engine_Size'))
        Cylinders = eval(data('Cylinders'))
        Transmission = data('Transmission')
        Fuel_Type = data('Fuel_Type')
        Fuel_Consumption_City1 = eval(data('Fuel_Consumption_City1'))
        Fuel_Consumption_Hwy1 = eval(data('Fuel_Consumption_Hwy1'))
        Fuel_Consumption_Comb2 = eval(data('Fuel_Consumption_Comb2'))
        Fuel_Consumption_Comb3 = eval(data('Fuel_Consumption_Comb3'))

        obj=Predict_CO2_Emission(make,model,Vehicle_Class, Engine_Size, Cylinders,Transmission, Fuel_Type
                  ,Fuel_Consumption_City1, Fuel_Consumption_Hwy1
                  ,Fuel_Consumption_Comb2, Fuel_Consumption_Comb3)
        predicted_co2 = obj.predicted_co2_emmission()

        #return jsonify({"Result":f"predicted co2 emmission : {predicted_co2}"})
        return render_template('co2_emmission1.html',prediction = predicted_co2 )
    
    elif request.method=='POST':

        data = request.form
        print('data : ',data)
        make = data['make']
        model = data['model']
        Vehicle_Class = data['Vehicle_Class']
        Engine_Size=eval(data['Engine_Size'])
        Cylinders = eval(data['Cylinders'])
        Transmission = data['Transmission']
        Fuel_Type = data['Fuel_Type']
        Fuel_Consumption_City1 = eval(data['Fuel_Consumption_City1'])
        Fuel_Consumption_Hwy1 = eval(data['Fuel_Consumption_Hwy1'])
        Fuel_Consumption_Comb2 = eval(data['Fuel_Consumption_Comb2'])
        Fuel_Consumption_Comb3 = eval(data['Fuel_Consumption_Comb3'])

        obj=Predict_CO2_Emission(make,model,Vehicle_Class, Engine_Size, Cylinders,Transmission, Fuel_Type
                  ,Fuel_Consumption_City1, Fuel_Consumption_Hwy1
                  ,Fuel_Consumption_Comb2, Fuel_Consumption_Comb3)
        predicted_co2 = obj.predicted_co2_emmission()

        #return jsonify({"Result":f"predicted co2 emmission : {predicted_co2}"})
        return render_template('co2_emmission1.html',prediction = predicted_co2 )
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.port_number)