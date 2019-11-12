from clarifai.rest import ClarifaiApp
from constants import MODEL_ID, API_KEY
import time 
import serial

arduinoData = serial.Serial('com4', 9600)

client = ClarifaiApp(api_key=API_KEY)
model = client.models.get(MODEL_ID)

def predict():
    prediction = model.predict_by_filename('test.jpg')
    outputs = prediction['outputs'][0]['data']['concepts']

    for concept in outputs:
        if concept['name'] == 'recycle' and float(concept['value']) >= 0.5:
                return 'recycle'
        elif concept['name'] == 'compost' and float(concept['value']) >= 0.5:
                return 'recycle'

    return 'landfill'


def main():
    label = predict()
    if(label == 'recycle'):
        arduinoData.write(b'0')
    elif(label == 'landfill'):
        arduinoData.write(b'1')
    print('The item identified is: ' + label)
    print('Finished executing script.')

if __name__ == '__main__':
    main()

