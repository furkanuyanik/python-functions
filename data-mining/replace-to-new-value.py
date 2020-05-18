def replace_to_new_value(data, column, old_value, new_value)
    return data[column].replace(to_replace=old_value, value=new_value, inplace=True)

def replace_to_mean(data, column, old_value):
    return data[column].replace(to_replace=old_value, value=data[column].mean(), inplace=True)
