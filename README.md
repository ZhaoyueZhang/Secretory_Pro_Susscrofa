# Secretory_Pro_Susscrofa
In this study, we proposed the first classification model to identify secretory proteins in Sus scrofa.
Based on the pseudo composition of k-spaced amino acid pairs feature encoding method and support vector machine algorithm, a prediction model was established for the identification of the secretory protein in Sus scrofa. 
The model produced the AUROC of 0.885 and 0.728 on the training set and independent testing set, respectively.

1. Download model at your computer with Linux system and 
    prepare your data in fasta format.

2. Type
    cd Libsvm_cvo && make clean && make
	
3. Type
    python3 pipeline.py test.fasta
	
4. Open res.txt to get the prediction result.
