def tp_fp(y_true, y_pred):
    
    # TP = sum(true == 1 & pred == 1 for true, pred in zip(y_true, y_pred))

    zip_list = []
    tp_list = []
    fp_list = []

    for i in range(len(y_true)):
        lst = []
        lst.append(y_true[i])
        lst.append(y_pred[i])
        zip_list.append(lst)
    # zip_list = [[1,1],[0,0], ... ,[1,1],[0,0]]

    # TP
    for j in range(len(zip_list)):
        if zip_list[j][0] == zip_list[j][1] == 1:
            tp_list.append(1)
        else:
            tp_list.append(0)
    
    # FP
    for j in range(len(zip_list)):
        if zip_list[j][0] < zip_list[j][1] :
            fp_list.append(1)
        else:
            fp_list.append(0)

    tp_sum = sum(tp_list)
    fp_sum = sum(fp_list)
    acc = tp_sum / (tp_sum + fp_sum)
    
    return tp_sum, fp_sum, acc

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 1, 0, 1, 0, 1, 1]

print("TP : {}\nFP : {}\nAccuracy : {}".format(tp_fp(y_true, y_pred)[0],tp_fp(y_true, y_pred)[1], tp_fp(y_true, y_pred)[2]))