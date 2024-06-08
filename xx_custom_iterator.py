
class MyIter:
  def __init__(self, limit: int) -> None:
    self.__limit = limit
    self.__counter = 0


  def __iter__(self):
    return self


  def __next__(self):
    if self.__counter >= self.__limit:
      raise StopIteration
    else:
      self.__counter += 1
      return self.__counter


itr = MyIter(5)

for i in itr:
  print(i)


