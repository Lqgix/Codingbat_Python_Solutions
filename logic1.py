def cigar_party(cigars, is_weekend):
  if(is_weekend == True):
    if(cigars >= 40):
      return True
    else:
      return False
  elif(is_weekend == False):
    if(cigars >= 40) and (cigars <= 60):
      return True
    else:
      return False  