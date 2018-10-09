import pickle as pk
import ujson as json
import numpy as np


class UnorderedLinker:
    def __init__(self, dataset_path, relations_path):
        with open(dataset_path, 'rb') as f_h:
            self.rel2id = pk.load(f_h, encoding='latin1')
            self.id2rel = {v[0]: ([k] + v[1:]) for k, v in self.rel2id.items()}

        with open(relations_path, 'rb') as f_h:
            self.core_chains = json.load(f_h)

    def __find_core_chain(self, question):
        for item in self.core_chains:
            if item['parsed-data']['corrected_question'] == question:
                return item
        return None

    def link(self, surface, question):
        core_chain = self.__find_core_chain(question)
        if core_chain is not None:
            hop_1 = core_chain['uri']['hop-1-properties']
            hop_2 = core_chain['uri']['hop-2-properties']
            hop_1 = [item[1] for item in hop_1]
            hop_2 = list(set([item[3] for item in hop_2]))
            results = [self.id2rel[id] for id in set(hop_1 + hop_2)]
            return results