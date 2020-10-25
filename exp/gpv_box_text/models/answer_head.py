import torch
import torch.nn as nn
import numpy as np

import utils.io as io


class AnswerHead(nn.Module):
    def __init__(
            self,
            vocab,
            hidden_dim,
            classifier_transform,
            vocab_embed=None):
        super().__init__()
        self.vocab = vocab

        if vocab_embed is None:
            vocab_embed = 0.1*torch.randn([len(self.vocab),hidden_dim])
        else:
            vocab_embed = torch.FloatTensor(vocab_embed)
            print('Using precomputed vocab embeddings')
        
        self.vocab_embed = nn.Parameter(vocab_embed,requires_grad=False)
        self.classifier_transform = classifier_transform

    def forward(self,answer_embed):
        """
        answer_embed: LxBxTxD
        """
        L,B,T,D = answer_embed.size()
        vocab_classifiers = self.classifier_transform(self.vocab_embed) # VxD
        vocab_classifiers = vocab_classifiers.permute(1,0).view(1,1,1,D,-1) # 1x1x1xDxV
        answer_embed = answer_embed.view(*answer_embed.size(),1) # LxBxTxDx1
        return torch.sum(vocab_classifiers*answer_embed,3) # LxBxTxV


def build_answer_head(cfg,classifier_transform):
    vocab_embed = None
    if cfg.vocab_embed is not None:
        vocab_embed = np.load(cfg.vocab_embed)
    
    vocab = io.load_json_object(cfg.vocab)
    return AnswerHead(
        vocab,
        cfg.detr.hidden_dim,
        classifier_transform,
        vocab_embed)



