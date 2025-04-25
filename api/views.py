from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.conf import settings
from django.http import HttpResponse

import numpy as np
import joblib  # we'll save and load the scaler using joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler


# === STEP 1: Load the trained model ===
model = load_model(os.path.join(settings.BASE_DIR,'artifacts','SleepApnea-predictor-spo2-pr.h5'))
import pandas as pd
df = pd.read_csv(os.path.join(settings.BASE_DIR,'artifacts','Oxygen Dataset Final.csv'))  # Replace with your actual dataset file

@csrf_exempt
def double_dict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            finalOut = getOutput(data)
            return HttpResponse(finalOut)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)



def getOutput(data):

    X = df[["spo2", "pr"]]  # same features used during training
    scaler = MinMaxScaler()
    scaler.fit(X)

    # === STEP 3: Create new input and scale it ===
    # Example input: spo2 = 95, pulse rate = 76
    # print(data,type(data))
    # return (data,type(data))
    new_data = np.array([[data["spo2"], data["pulse"]]])  # shape = (1, 2)
    new_data_scaled = scaler.transform(new_data)

    # === STEP 4: Make a prediction ===
    prediction = model.predict(new_data_scaled)

    # === STEP 5: Interpret and print the result ===
    prob = prediction[0][0]
    if prob > 0.5:
        print(f"High chance of sleep apnea (probability = {prob:.2f})")
        return(f"High chance of sleep apnea (probability = {prob:.2f})") 
    else:
        print(f"Low chance of sleep apnea (probability = {prob:.2f})")
        return(f"Low chance of sleep apnea (probability = {prob:.2f})")