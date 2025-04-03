import torch 
print(torch.cuda.is_available())
if torch.cuda.is_available():
    print("Cuda is Available")
else:
    print("Cuda Can't be found")