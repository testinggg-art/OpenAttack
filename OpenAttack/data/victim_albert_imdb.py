"""
:type: OpenAttack.utils.AlbertClassifier
:Size: 788.662MB
:Package Requirements:
    * transformers
    * pytorch

Pretrained ALBERT model on IMDB dataset. See :py:data:`Dataset.IMDB` for detail.
"""

from OpenAttack.utils import make_zip_downloader

NAME = "Victim.ALBERT.IMDB"

URL = "https://cdn.data.thunlp.org/TAADToolbox/victim/albert_imdb.zip"
DOWNLOAD = make_zip_downloader(URL)

def LOAD(path):
    from OpenAttack import HuggingfaceClassifier
    import transformers
    tokenizer = transformers.AutoTokenizer.from_pretrained(path)
    model = transformers.AutoModelForSequenceClassification.from_pretrained(path, num_labels=2, output_hidden_states=False)
    return HuggingfaceClassifier(model, tokenizer=tokenizer, max_len=100, embedding_layer=model.albert.embeddings.word_embeddings)