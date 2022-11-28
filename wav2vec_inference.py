from transformers.file_utils import cached_path, hf_bucket_url
import os, zipfile
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import load_dataset
import soundfile as sf
import torch
import kenlm
from pyctcdecode import Alphabet, BeamSearchDecoderCTC, LanguageModel


def get_decoder_ngram_model(tokenizer, ngram_lm_path):
    vocab_dict = tokenizer.get_vocab()
    sort_vocab = sorted((value, key) for (key, value) in vocab_dict.items())
    vocab = [x[1] for x in sort_vocab][:-2]
    vocab_list = vocab
    # convert ctc blank character representation
    vocab_list[tokenizer.pad_token_id] = ""
    # replace special characters
    vocab_list[tokenizer.unk_token_id] = ""
    # vocab_list[tokenizer.bos_token_id] = ""
    # vocab_list[tokenizer.eos_token_id] = ""
    # convert space character representation
    vocab_list[tokenizer.word_delimiter_token_id] = " "
    # specify ctc blank char index, since conventially it is the last entry of the logit matrix
    alphabet = Alphabet.build_alphabet(vocab_list, ctc_token_idx=tokenizer.pad_token_id)
    lm_model = kenlm.Model(ngram_lm_path)
    decoder = BeamSearchDecoderCTC(alphabet,
                                   language_model=LanguageModel(lm_model))
    return decoder


class Wav2vecInference:
    def __init__(self, cache_dir: str, beam_width: int = 500):
        self.processor = Wav2Vec2Processor.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h",
                                                      cache_dir=cache_dir)
        self.model = Wav2Vec2ForCTC.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h", cache_dir=cache_dir)
        lm_file = hf_bucket_url("nguyenvulebinh/wav2vec2-base-vietnamese-250h", filename='vi_lm_4grams.bin.zip')
        lm_file = cached_path(lm_file, cache_dir=cache_dir)
        with zipfile.ZipFile(lm_file, 'r') as zip_ref:
            zip_ref.extractall(cache_dir)
        self.lm_file = cache_dir + 'vi_lm_4grams.bin'
        self.tokenizer = self.processor.tokenizer
        self.ngram_lm_model = get_decoder_ngram_model(self.tokenizer, self.lm_file)
        self.beam_width = beam_width


    def inference(self, data, sample_rate):
        input_values = self.processor(data, sampling_rate=sample_rate, return_tensors="pt").input_values
        logits = self.model(input_values).logits[0]
        pred_ids = torch.argmax(logits, dim=-1)
        # greedy_search_output = self.processor.decode(pred_ids)
        beam_search_output = self.ngram_lm_model.decode(logits.cpu().detach().numpy(), beam_width=self.beam_width)
        return beam_search_output

