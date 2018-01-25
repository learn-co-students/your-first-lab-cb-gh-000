def my_all?(collection)
  i = 0
  while i < collection.length
    i = i + 1   #i += 1 does the same thing. Use this if it's easier for you.
  end
end

def my_all?(collection)
  i = 0
  while i < collection.length
    yield(collection[i])
    i = i + 1
  end
end

my_all?([1,2,3]) {|i| i < 2}
