def fetch_details(df_list, director=False, character=False):

    if character:
        characters = [item['character'] for item in df_list]
        return ', '.join(characters)

    if director:
        for dir in df_list:
            if dir['job'] == 'Director':
                return dir["name"]
            else:
                break

    names = [item['name'] for item in df_list]
    return ', '.join(names)

def customer_scaler(x, max):
    return (x/max) * 10