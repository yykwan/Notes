# AlphaEvolve: A Learning Framework to Discover Novel Alphas in Quantitative Investment
Alphas are stock prediction models generating trading signals  
Aim: identify a set of weakly correlated formulaic alphas with high returns  
Limitations of genetic algorithms: small algorithm search space, only searches formulaic alphas which only utilize short-term features  

## Components of Alphas:  
1. a setup function to initialize operands
2. a predict function to generate a prediction
3. a parameter-updating function to update parameters ( if any parameters are generated during evolution )

## Prediction Function
->improves the formulaic alphas by extracting features from vectors and matrices  
->includes scalars in operations -> less complex than machine learning alphas  
->features of long-term training -> improves the alpha's inference ability  

## Optimization
stocks predicted are classified into sectors and industries in a stock market  
->improves the prediction accuracy  
RelationOps:  
calculate an output operand based on input scalar operands calculated in the current task and other related tasks in the same sector  
ExtractionOps:  
facilitate searching for the new class of alphas + avoid discovering a complex machine learning alpha from scratch  
## Pruning Technique
Before:  
fingerprints an alpha by its predictions on a small set of samples and uses the fingerprint to terminate any repeated alphas with the same predictions on the set of samples in subsequent searches -> inefficient  
### Redundancy Pruning Process: prunes the operations that do not contribute to the calculation  
1. represent an alpha as a graph with operatprs as edges and operands as nodes
2. check a node's redundancy by finding the operation where the node is the output operand and check if the input operands of this operation are redundant nodes
3. prune the operation with a redundant output operand
-> an alpha with no redundancy tends to be vulnerable to random mutations



