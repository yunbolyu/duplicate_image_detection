from pathlib import Path
import imagededup
from imagededup.methods import CNN
from imagededup.evaluation import evaluate

image_dir = Path('../tests/data/test_lisa')

cnn_encoder = CNN()
duplicates_cnn = cnn_encoder.find_duplicates(image_dir=image_dir, min_similarity_threshold=0.97)

print(duplicates_cnn)
