import torch.nn as nn
import torchvision.models as models

from utils import NUM_PTS, CROP_SIZE


def create_model():
    model = models.densenet169(pretrained=True)

    model.classifier = nn.Linear(model.classifier.in_features, 2 * NUM_PTS, bias=True)
    return model
