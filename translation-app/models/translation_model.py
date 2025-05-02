# If using a downloaded pretrained model

from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self, src_lang="ar", tgt_lang="en"):
        self.set_languages(src_lang, tgt_lang)

    def set_languages(self, src_lang, tgt_lang):
        model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text):
        tokens = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = self.model.generate(**tokens)
        return self.tokenizer.decode(translated[0], skip_special_tokens=True)