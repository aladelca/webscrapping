from utils.read_files import read_pickle



def predict(model_path, vect_path, input):
    model = read_pickle(model_path)
    vect = read_pickle(vect_path)
    return model.predict(vect.transform([input]))[0]