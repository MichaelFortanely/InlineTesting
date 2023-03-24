import find_features

import numpy as np
import pandas as pd

def run_tree(file_name):
    arr=np.load(file_name)
    x=np.ndarray.tolist(arr)
    print(len(x))
    print(x[0])
    print(len(x[0]))

    x[0].extend(['is_keyword', 'length', 'is_regular_expression', 'is_mathematical_calculation',
            'is_collection_manipulation', 'is_string_manipulation', 'is_bit_manipulation','is_variable_assignment'])
    
    for i in range(1,len(x)-1):
        item=x[i]
        line=item[1]
        keyword=find_features.is_keyword(line)
        length=find_features.length(line)
        regex=find_features.is_regular_expression(line)
        math=find_features.is_mathematical_calculation(line)
        coll=find_features.is_collection_manipulation(line)
        str_manipulate=find_features.is_string_manipulation(line)
        bit=find_features.is_bit_manipulation(line)
        var=find_features.is_variable_assignment(line)

        item.extend([keyword, length, regex, math, coll, str_manipulate, bit, var])

    print(x)

    # np.savetxt("example.csv", x, delimiter=",")
    pd.DataFrame(x).to_csv("example.csv")
    return np.array(x)

run_tree("./simple_data.npy")