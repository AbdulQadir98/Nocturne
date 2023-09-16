import torch
from transformers import BertTokenizer
import torch.nn as nn
from transformers import AutoModel

class BERT_Arch(nn.Module):
    def __init__(self, bert):
      super(BERT_Arch, self).__init__()
      self.bert = bert
      self.dropout = nn.Dropout(0.1)
      self.relu =  nn.ReLU()
      self.fc1 = nn.Linear(768,512)
      self.fc2 = nn.Linear(512,2)
      self.softmax = nn.LogSoftmax(dim=1)
    def forward(self, sent_id, mask):
      _, cls_hs = self.bert(sent_id, attention_mask=mask, return_dict=False)
      x = self.fc1(cls_hs)
      x = self.relu(x)
      x = self.dropout(x)
      x = self.fc2(x)
      x = self.softmax(x)
      return x


def modelPrediction(text):
  bert = AutoModel.from_pretrained('bert-base-uncased')
  model_name = 'bert-base-uncased'
  tokenizer = BertTokenizer.from_pretrained(model_name)
  model = BERT_Arch(bert)
  path_to_weights = '../assets/saved_weights.pt'
  model.load_state_dict(torch.load(path_to_weights, map_location=torch.device('cpu')))
  input_text = text
  tokens = tokenizer(input_text, padding=True, truncation=True, return_tensors="pt")
  with torch.no_grad():
      outputs = model(tokens['input_ids'], tokens['attention_mask'])
  logits = outputs
  predicted_class = torch.argmax(logits, dim=1).item()
  return predicted_class
