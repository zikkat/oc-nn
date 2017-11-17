import os
cwd = os.getcwd()
import sys
sys.path.append(cwd)
print cwd

# Import all the models functions
from sklearn_OCSVM_model import sklearn_OCSVM_linear, sklearn_OCSVM_rbf
from OneClass_NN_model import One_Class_NN_explicit_linear, One_Class_NN_explicit_sigmoid
from sklearn_OCSVM_explicit_model import sklearn_OCSVM_explicit_linear, sklearn_OCSVM_explicit_sigmoid
from tf_OneClass_NN_model import tf_OneClass_NN_linear, tf_OneClass_NN_sigmoid
from tf_OneClass_CNN_model import tf_OneClass_CNN_linear, tf_OneClass_CNN_sigmoid
from tflearn_OneClass_NN_model import tflearn_OneClass_NN_linear, tflearn_OneClass_NN_Sigmoid

# Declare a dictionary to store the results
df_cifar_scores = {}


def func_getDecision_Scores_cifar(dataset, data_train, data_test, labels_train, data, data_train_ocsvm, data_test_ocsvm):

    # sklearn_OCSVM
    result = sklearn_OCSVM_linear(data_train_ocsvm, data_test_ocsvm)
    df_cifar_scores["sklearn-OCSVM-Linear-Train"] = result[0]
    df_cifar_scores["sklearn-OCSVM-Linear-Test"] = result[1]

    result = sklearn_OCSVM_rbf(data_train_ocsvm, data_test_ocsvm)
    df_cifar_scores["sklearn-OCSVM-RBF-Train"] = result[0]
    df_cifar_scores["sklearn-OCSVM-RBF-Test"] = result[1]
    print ("Finished sklearn_OCSVM_linear")

    # sklearn _OCSVM_explicit
    result = sklearn_OCSVM_explicit_linear(data_train_ocsvm, data_test_ocsvm)
    df_cifar_scores["sklearn-OCSVM-explicit-Linear-Train"] = result[0]
    df_cifar_scores["sklearn-OCSVM-explicit-Linear-Test"] = result[1]

    result = sklearn_OCSVM_explicit_sigmoid(data_train_ocsvm, data_test_ocsvm)
    df_cifar_scores["sklearn-OCSVM-explicit-Sigmoid-Train"] = result[0]
    df_cifar_scores["sklearn-OCSVM-explicit-Sigmoid-Test"] = result[1]

    print ("Finished sklearn _OCSVM_explicit")

    # #One Class NN Explicit
    # result = One_Class_NN_explicit_linear(data_train_ocsvm,data_test_ocsvm)
    # df_cifar_scores["One_Class_NN_explicit-Linear-Train"] = result[0]
    # df_cifar_scores["One_Class_NN_explicit-Linear-Test"] =  result[1]

    # result = One_Class_NN_explicit_sigmoid(data_train_ocsvm,data_test_ocsvm)
    # df_cifar_scores["One_Class_NN_explicit-Sigmoid-Train"] = result[0]
    # df_cifar_scores["One_Class_NN_explicit-Sigmoid-Test"] = result[1]

    # print ("Finished One Class NN Explicit")

    # result = tf_OneClass_NN_linear(data_train_ocsvm,data_test_ocsvm)
    # df_cifar_scores["tf_OneClass_NN-Linear-Train"] = result[0]
    # df_cifar_scores["tf_OneClass_NN-Linear-Test"] =  result[1]

    # result = tf_OneClass_NN_sigmoid(data_train_ocsvm,data_test_ocsvm)
    # df_cifar_scores["tf_OneClass_NN-Sigmoid-Train"] = result[0]
    # df_cifar_scores["tf_OneClass_NN-Sigmoid-Test"] = result[1]

    result = tf_OneClass_CNN_linear(data_train, data_test, data)
    df_cifar_scores["tf_OneClass_CNN-Linear-Train"] = result[0]
    df_cifar_scores["tf_OneClass_CNN-Linear-Test"] = result[1]

    # result = tf_OneClass_CNN_sigmoid(data_train,data_test)
    # df_cifar_scores["tf_OneClass_CNN-Sigmoid-Train"] = result[0]
    # df_cifar_scores["tf_OneClass_CNN-Sigmoid-Test"] = result[1]

    print ("Finished tf_OneClass_CNN_linear")

    # Y = labels_train
    # labels_train = [[i] for i in Y]
    # result = tflearn_OneClass_NN_linear(data_train,data_test,labels_train)
    # df_cifar_scores["tflearn_OneClass_NN-Linear-Train"] = result[0]
    # df_cifar_scores["tflearn_OneClass_NN-Linear-Test"] =  result[1]

    # result = tflearn_OneClass_NN_Sigmoid(data_train,data_test,labels_train)
    # df_cifar_scores["tflearn_OneClass_NN-Sigmoid-Train"] = result[0]
    # df_cifar_scores["tflearn_OneClass_NN-Sigmoid-Test"] = result[1]
    # print ("Finished tflearn_OneClass")

    # print (type(df_cifar_scores))
    # print ( (df_cifar_scores.keys()))

    return df_cifar_score