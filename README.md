# MDP-Parser
The main objective of this project is to find the mention of entities and relation given a natural language question and underlying knowledge graph. It further use a simple index-based linking to link the mentions into the item from the knowledge graph. 


## Train
Parameters
--epochs
--dropout
--lr 
--batchsize
--k
--mode (train/test) 
--dataset (lcquad/qald_7_ml) 
--b (number of prev/next words)
--checkpoint filename 
--policy (lstm/bilstm/nn)

Sample run command:
```
python scripts/execute.py --epochs 50  --dropout 0.1 --lr 0.0001 --batchsize 1 --k 10 --mode train --dataset qald_7_ml --b 1 --checkpoint tmp --policy nn
```

## Cite
If you would use the codebase, please cite our paper as well:

```
@article{zafar2019mdp,
  title={MDP-based Shallow Parsing in Distantly Supervised QA Systems},
  author={Zafar, Hamid and Tavakol, Maryam and Lehmann, Jens},
  journal={arXiv preprint arXiv:1909.12566},
  year={2019}
}
```

## Live Demo
Coming soon! Stay tuned!
