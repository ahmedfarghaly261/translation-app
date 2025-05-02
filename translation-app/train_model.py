
from datasets import load_dataset
from transformers import MarianMTModel, MarianTokenizer, Seq2SeqTrainer, Seq2SeqTrainingArguments

# Load TSV file and convert to dataset
with open("data/arabic_english.tsv", "r", encoding="utf-8") as f:
    lines = f.readlines()

texts = [line.strip().split("\t") for line in lines if "\t" in line]

data = {"translation": [{"ar": ar, "en": en} for ar, en in texts]}

def split_data(data, split_ratio=0.9):
    split_point = int(len(data["translation"]) * split_ratio)
    return {
        "train": data["translation"][:split_point],
        "test": data["translation"][split_point:]
    }

splits = split_data(data)

# Define tokenizer and model
src_lang = "ar"
tgt_lang = "en"
model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def preprocess(example):
    src = tokenizer(example[src_lang], padding="max_length", truncation=True, return_tensors="pt")
    with tokenizer.as_target_tokenizer():
        tgt = tokenizer(example[tgt_lang], padding="max_length", truncation=True, return_tensors="pt")
    return {
        "input_ids": src["input_ids"].squeeze(),
        "attention_mask": src["attention_mask"].squeeze(),
        "labels": tgt["input_ids"].squeeze()
    }

train_data = list(map(preprocess, splits["train"]))
test_data = list(map(preprocess, splits["test"]))

training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    learning_rate=5e-5,
    num_train_epochs=3,
    logging_dir="./logs",
    save_strategy="epoch",
    evaluation_strategy="epoch"
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
)

trainer.train()

model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")