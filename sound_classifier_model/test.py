import librosa
from tensorflow import keras
import numpy as np
max_pad_len = 174

def extract_feature(file_name):
    print('file name :', file_name)
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        pad_width = max_pad_len - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0,0), (0, pad_width)), mode='constant')
        print(mfccs.shape)
        
    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        print(e);
        return None
    
#     return padded_mfccs
    return mfccs

def predict():
    # Load the model
    loaded_model = keras.models.load_model('/home/kimmokalover/바탕화면/hackerton/sound_classifier_model/sound_classifier_model')

    filename = "/home/kimmokalover/바탕화면/hackerton/recorded.wav"
    mfccs = extract_feature(filename)
    # print(mfccs)
    mfccs = np.reshape(mfccs, (-1, 40, 174, 1))
    predictions = loaded_model.predict(mfccs)
    class_names = ["air_conditioner", "car_horn", "children_playing", "dog_bark", "drilling", "engine", "gun_shot", "jackhammer", "siren", "street_music"]
    print("------------------------------------------------------")
    # print(predictions)

    predicted_index = np.argmax(predictions)
    predicted_class = class_names[predicted_index]
    print("Predicted class is:", predicted_class)
    print("-------------------------------------------------------")
    return predicted_class


predict()
