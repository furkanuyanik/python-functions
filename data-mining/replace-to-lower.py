def set_to_lower(data):
  for item in data.columns:
    try: data[item] = data[item].str.lower()
    except: continue
  return data