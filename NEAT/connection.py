class Connection:
  def __init__(self, start, end, weight, innov_num, enabled=True):
    self.start = start
    self.end = end
    self.weight = float(weight)
    self.innov_num = int(innov_num)
    self.enabled = bool(enabled)

    #adds input connections to nodes
    self.end.append_in(self.start)

    #addes output connection to nodes
    self.start.append_out(self.end)


  def __eq__(self, other):
    
    #not same type
    if not (type(other) == Connection):
      return False

    return(self.__dict__ == other.__dict__)

  def __repr__(self):
    return f"Connection {self.innov_num:02} goes from {self.start.num:02} to {self.end.num:02}. Has a weight of {self.weight:.2f} and is {self.enabled}"

class Connection_genome(list):
  def __init__(self):
    list.__init__([])  

  def __repr__(self):
    out = ""
    for i in self:
      out = out+(i.__repr__()+"\n")

    out = out[:-1]
    return out
  def append(self, connection):
    if type(connection) == Connection:
      list.append(self, connection)
      
    else:
      raise NotImplementedError(f"Wrong type '{connection}'")
  def __getitem__(self, item):
    if type(item) == int:
      return list.__getitem__(self, item)

    if type(item) == Connection:
      for i, conn in enumerate(self):
        if conn == item:
          return i
          
    else:
      raise TypeError("Wrong type "+item)