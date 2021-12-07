import pickle


def save_audio_file_number(audio_file_number):
    try:
        with open("/tmp/data.pickle", "wb") as f:
            pickle.dump(audio_file_number, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def get_audio_file_number():
    filename = "/tmp/data.pickle"
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

