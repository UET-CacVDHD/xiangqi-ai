from fastapi import FastAPI, UploadFile
import uvicorn
from wav2vec_inference import Wav2vecInference


wav2vec_model = Wav2vecInference(cache_dir="./cache/", lm_file="lm.arpa")
app = FastAPI()


@app.post("/predict")
def predict(file: UploadFile):
    output = wav2vec_model.file_to_text(file.file)
    return output


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=False)
