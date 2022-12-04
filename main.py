from fastapi import FastAPI, UploadFile, File
import uvicorn
from wav2vec_inference import Wav2vecInference
from command_converter import convert_text_to_command


wav2vec_model = Wav2vecInference(lm_file="lm_4.arpa")
app = FastAPI()


@app.post("/predict")
def predict(file: UploadFile = File()):
    output = wav2vec_model.file_to_text(file.file)
    command = convert_text_to_command(output[1])
    return output, command


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
