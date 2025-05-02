import os
os.makedirs("data", exist_ok=True)

with open("./data/Tatoeba.ar-en.ar", "r", encoding="utf-8") as ar_file, \
    open("./data/Tatoeba.ar-en.en", "r", encoding="utf-8") as en_file, \
    open("data/arabic_english.tsv", "w", encoding="utf-8") as out_file:

    for ar_line, en_line in zip(ar_file, en_file):
        ar_line = ar_line.strip()
        en_line = en_line.strip()
        if ar_line and en_line:
            # Write tab-separated sentence pair
            out_file.write(f"{ar_line}\t{en_line}\n")