import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
lst += ['cat'] * 10
lst += ['dog'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
onehot_data = pd.DataFrame(columns=['whoAmI_' + str(i) for i in pd.unique(data['whoAmI'])])
for i in data.iloc:
    for j in onehot_data.columns:
        if i.item() in j:
            index = len(onehot_data.index)
            onehot_data.loc[index] = False
            onehot_data.loc[index, j] = True
print(onehot_data)
