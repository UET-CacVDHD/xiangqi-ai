from pydub import AudioSegment
import kenlm
from pyctcdecode import Alphabet, BeamSearchDecoderCTC, LanguageModel
import secrets


def get_random_string(nbytes: int = 20):
    return secrets.token_hex(nbytes)


def convert_audio_to_wav(source_file: str, des_file: str):
    track = AudioSegment.from_file(source_file)
    file_handle = track.export(des_file, format="wav")


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


if __name__ == "__main__":
    convert_audio_to_wav("A.mp3", "A.wav")
