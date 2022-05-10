import os
from regex import F
import torch
import torchvision
import torchvision.transforms as transforms 

path = './train_images_100'

transformation = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor()])
dataset = torchvision.datasets.ImageFolder(root = path, transform=transformation)
train_loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=32, shuffle=False)

def getMean(loader):
    mean = 0.0
    std = 0.0
    total_image_count = 0
    
    for images, _ in loader:
        imageCount = images.size(0)
        images = images.view(imageCount, images.size(1), -1)
        mean += images.mean(2).sum(0)
        std += images.std(2).sum(0)
        total_image_count += imageCount
        
    mean /= total_image_count
    std /= total_image_count
    
    return mean, std

mean, std = getMean(train_loader)

print (mean)
print (std)