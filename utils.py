import pickle
import json
import pandas as pd
import numpy as np
import config

class Predict_CO2_Emission():
    def __init__(self,make,model,Vehicle_Class, Engine_Size, Cylinders,Transmission, Fuel_Type
                  ,Fuel_Consumption_City1, Fuel_Consumption_Hwy1
                  ,Fuel_Consumption_Comb2, Fuel_Consumption_Comb3):
        self.make = make
        self.model = model
        self.Vehicle_Class = Vehicle_Class
        self.Engine_Size = Engine_Size
        self.Cylinders = Cylinders
        self.Transmission = Transmission
        self.Fuel_Type = Fuel_Type
        self.Fuel_Consumption_City1 = Fuel_Consumption_City1
        self.Fuel_Consumption_Hwy1 = Fuel_Consumption_Hwy1
        self.Fuel_Consumption_Comb2 = Fuel_Consumption_Comb2
        self.Fuel_Consumption_Comb3 = Fuel_Consumption_Comb3

    def __get_data(self):
        with open(config.model_file_path, 'rb') as f:
            self.model = pickle.load(f)
        with open(config.json_file_path,'r') as f:
            self.columns_list = json.load(f)


    def get_input_row(self):
        self.__get_data()
        df1=pd.DataFrame(np.zeros(shape=(50)))
        df1.index=self.columns_list['columns_x']
        self.df2=df1.T
        self.df2['Engine Size(L)']=self.Engine_Size
        self.df2['Cylinders']=self.Cylinders
        self.df2['Fuel Consumption City (L/100 km)']=self.Fuel_Consumption_City1
        self.df2['Fuel Consumption Hwy (L/100 km)']=self.Fuel_Consumption_Hwy1
        self.df2['Fuel Consumption Comb (L/100 km)']=self.Fuel_Consumption_Comb2
        self.df2['Fuel Consumption Comb (mpg)']=self.Fuel_Consumption_Comb3
        self.df2['Fuel Type']=self.Fuel_Type
        col_name='Vehicle Class_'+ self.Vehicle_Class    
        self.df2[col_name]= 1
        col_name1='Transmission_'+ self.Transmission
        self.df2[col_name1]=1
        self.df2['Fuel Type'].replace({'Z':3, 'D':5, 'X':4, 'E':2, 'N':1},inplace=True)
        return self.df2

    def predicted_co2_emmission(self):
        self.get_input_row()
        y_predicted = self.model.predict(self.df2)
        predicted_co2= y_predicted[0][0]
        return predicted_co2