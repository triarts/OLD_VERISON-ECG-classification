# check latest script
google drive link : https://drive.google.com/open?id=1BT_A6GxjFPWxMZXknBx-S5hJ4EqRs2ZJ
flask deployment based on this tutorial : https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2

# ECG-classification
* Kaggle dataset : https://www.kaggle.com/shayanfazeli/heartbeat
  * direct download from : https://drive.google.com/open?id=1uBsf_3kGqYoHUccYYArNquejQZhEsz-u
    * MIT-BIH(5 class) and PTB(2 class) 
* Physionet mit-bih : https://www.physionet.org/physiobank/database/mitdb/
### code from : 
#### Using kaggle dataset : 
  * test_final.ipynb = https://github.com/CVxTz/ECG_Heartbeat_Classification/blob/master/code/baseline_mitbih.py
  * https://github.com/mmontana/ECG-heartbeat-classification note: ada teknik smoothingnya
  * mathlab and python (SVM) vv : https://github.com/mondejar/ecg-classification 
    * note: penjelasannya cukup jelas
    * paper : https://ieeexplore.ieee.org/document/1306572 
    * di pake di hich : Empowering Healthcare IoT Systems with Hierarchical Edge-based Deep Learning
#### Using physionet MITBIH -> signal -> wfdb library
  * https://github.com/Fabrizio1994/ECGClassification
  
#### mitbih db to csv to 187 beat adn 188 as label  
  * https://github.com/koen-aerts/ECG_ML
  note: ini preprocessing yg di pake CVxTz
  
#### Using physionet MITBIH .atr (2D convolutional) vv
 * https://github.com/ankur219/ECG-Arrhythmia-classification
 * https://github.com/irakaundal/arrhythmia-cnn
 
#### other
 * https://github.com/SajadMo/ECG-Heartbeat-Classification-seq2seq-model
 * https://github.com/GrayLand119/ECG-ArrhythmiaClassification
 * [https://github.com/daimenspace/ECG-arrhythmia-classification-using-a-2-D-convolutional-neural-network](https://github.com/daimenspace/ECG-arrhythmia-classification-using-a-2-D-convolutional-neural-network.)
 * https://github.com/YeongHyeon/Arrhythmia_Detection_RNN_and_Lyapunov
 
### mimic and other dataset
 * https://archive.physionet.org/physiobank/database/

## reference 
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4897569/
* AAMI class reference : https://www.sciencedirect.com/science/article/pii/S0169260715003314
https://www.researchgate.net/figure/Mapping-the-MIT-BIH-Arrhythmia-types-to-the-AAMI-Classes_tbl1_267411759
