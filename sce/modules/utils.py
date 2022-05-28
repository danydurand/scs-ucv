
def navegation(idxx, keys):
    if len(keys) > 0:
        this_item = keys.index(idxx) 
        prev_item = this_item - 1 if this_item > 0 else 0
        next_item = this_item + 1 if this_item < len(keys)-1 else len(keys)-1
        return [keys[prev_item], keys[next_item]]
    else:
        return [None, None]
