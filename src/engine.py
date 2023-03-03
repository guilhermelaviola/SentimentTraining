from tqdm import tqdm

# Still needs the dataset.py file in order for it to be continued
def train_function(data_loader, model, optimizer, device, scheduler):
    model.train()

    for bi, d in tqdm(enumerate(data_loader), lotal=len(data_loader)):
        # To de done

def evaluation_function(data_loader, model, device):
    pass