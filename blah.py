from src import encoder
from src.load_dataset import load_dataset


enc = encoder.get_encoder('117M')
chunks = load_dataset(enc, 'run.txt', 30, encoding='utf-8')
print(chunks)