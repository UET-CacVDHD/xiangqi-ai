from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import soundfile as sf
import torch
from utils import convert_audio_to_wav, get_decoder_ngram_model, get_random_string
import os
import librosa


class Wav2vecInference:
    def __init__(self, lm_file: str, beam_width: int = 500):
        self.processor = Wav2Vec2Processor.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h")
        self.model = Wav2Vec2ForCTC.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h")

        self.lm_file = lm_file
        self.tokenizer = self.processor.tokenizer
        self.ngram_lm_model = get_decoder_ngram_model(self.tokenizer, self.lm_file)
        self.beam_width = beam_width
        self.sample_rate = 16000

    def inference(self, data, sample_rate):
        input_values = self.processor(data, sampling_rate=sample_rate, return_tensors="pt").input_values
        with torch.no_grad():
            logits = self.model(input_values).logits[0]
        pred_ids = torch.argmax(logits, dim=-1)
        greedy_search_output = self.processor.decode(pred_ids)
        beam_search_output = self.ngram_lm_model.decode(logits.cpu().detach().numpy(), beam_width=self.beam_width)
        return greedy_search_output, beam_search_output

    def file_to_text(self, file):
        tmp_file = f"./tmp/tmp_{get_random_string()}.wav"
        convert_audio_to_wav(file, tmp_file)
        audio_input, samplerate = librosa.load(tmp_file, sr=self.sample_rate)
        assert samplerate == self.sample_rate
        os.remove(tmp_file)
        return self.inference(audio_input, samplerate)


if __name__ == "__main__":
    pass
    # wav2vec_model = Wav2vecInference(lm_file="lm.arpa")
    # output = wav2vec_model.file_to_text("A.wav")
    # print(output)
