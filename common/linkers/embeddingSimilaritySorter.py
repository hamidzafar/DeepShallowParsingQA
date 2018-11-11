from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch
import torch.nn as nn


class EmbeddingSimilaritySorter:
    def __init__(self, word_vectorizer):
        self.word_vectorizer = word_vectorizer
        emb_shape = self.word_vectorizer.emb.shape
        self.emb = nn.Embedding(emb_shape[0], emb_shape[1], padding_idx=0, sparse=False)
        self.emb.weight.data.copy_(word_vectorizer.emb)

    def sort(self, surface, question, candidates):
        surface_embeddings = self.word_vectorizer.decode(surface)
        surface_embeddings = torch.mean(surface_embeddings, dim=0).reshape(1, -1)

        tmp = [item[5] for item in candidates]
        lens = torch.FloatTensor([len(item) for item in tmp]).reshape(-1, 1)
        candidates_coded = torch.zeros([len(tmp), max([len(item) for item in tmp])], dtype=torch.long)
        for idx, item in enumerate(tmp):
            candidates_coded[idx][:len(item)] = item
        if torch.cuda.is_available():
            candidates_coded = candidates_coded.cuda()
            lens = lens.cuda()
        candidates_embeddings = self.emb(candidates_coded)
        candidates_embeddings_mean = torch.sum(candidates_embeddings, dim=1) / lens
        candidates_similarity = torch.nn.functional.cosine_similarity(surface_embeddings, candidates_embeddings_mean)
        sorted_idx = np.argsort(candidates_similarity.data.numpy())[::-1]
        sorted = [candidates[idx] for idx in sorted_idx]
        return sorted
