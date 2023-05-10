import torch
from PIL import Image
import torchvision.transforms as transforms


def classify(image_file):
    device = torch.device('cpu')
    seefood = torch.load('seefood_resnet50.pth', map_location=device)
    image = Image.open(image_file)
    seefood.eval()

    transform = transforms.ToTensor()
    tensor = transform(image)
    tensor = tensor
    tensor = tensor.unsqueeze(dim=0)

    with torch.no_grad():
        output = seefood(tensor)
    _, predicted = torch.max(output, 1)

    labels = {0: 'borsch', 1: 'four cheeses', 2: 'khinkali', 3: 'pancake', 4: 'pelmeni', 5: 'pepperoni', 6: 'shawarma',
              7: 'shchi'}

    for key in labels.keys():
        if predicted == key:
            return labels[key]
