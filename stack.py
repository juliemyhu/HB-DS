class Stack():
    
    def __init__(self):
        self.stack = []
        self.current_max = float("-inf")

    def push(self,number):
        
        if number > self.current_max:
            self.current_max = number
        self.stack.append((number,self.current_max))

    def peek(self):
        return self.stack[-1]
    
    def pop(self):

        top = self.peek()
        if top[1] != self.stack[-2]:
            self.current_max = self.stack[-2][1]
        self.stack.pop()

    def is_empty(self):
        return self.stack is None 

    def max(self):
        return self.current_max
    

    
s1 = Stack()
s1.push(15)
s1.push(54)
s1.push(-63)
s1.push(2)
s1.push(32)

s2 = Stack()
s2.push(1)
s2.push(2)
s2.push(3)
s2.push(4)
s2.push(5)



def dfs(maze): # return true if you can get through the maze and false otherwise
  end = (len(maze) - 1, len(maze[-1]) - 1)
  
  stack = Stack()
  stack.push( (0, 0) ) 

  visited = [ [False for _ in maze[0]] for _ in maze]

  visited[0][0] = True
  num_rows = len(maze)
  num_cols = len(maze[-1])

  while len(stack) != 0:
    # current_pos = stack.peek() # (1, 3)
    i, j = stack.peek() # x=1 y=3

    # x is the row you are in
    # y is the col you are in

    # tuples are immutable 
    # print(i, j)
    stack.pop()
    if (i,j) == end:
      return True
    
    # check if next direction is o and false (and it is inside the maze)
    # right
    # check if the square to the right is in the maze, o, and hasnt been seen. add it to the stack if so

    # i is the row, j is the col. 
    # increasing i goes down in the maze, increasing j goes right
    # we know that i and j are valid indices
    # right
    if 0 <= j+1 < num_cols: # then i, j+1 is a valid index
      if maze[i][j+1] == "o" and visited[i][j+1] == False:
        stack.push( (i,j+1) )
        visited[i][j+1] = True
        # print("stuck?")

    #  Down 
    if 0 <= i+1 < num_rows: 
      if maze[i+1][j] == "o" and visited[i+1][j] == False:
        stack.push( (i+1,j))
        visited[i+1][j] = True
        # print("stuck also")
  
    # Left
    if 0 <= j-1 < num_cols:
      if maze[i][j-1] == "o" and visited[i][j-1] == False:
        stack.push( (i,j-1) )
        visited[i][j-1] = True
        # print("why?)

    if 0 <= i-1 < num_rows:
      if maze[i-1][j] == "o" and visited[i-1][j] == False:
        stack.push( (i-1,j) )
        visited[i-1][j] = True
                    # right.   up.     down.    left
    for direction in [(0,1), (0, -1), (1, 0), (-1, 0)]:
      x, y = direction # x = 0 y = 1
      if 0 <= i+x < num_rows and 0 <= j+y < num_cols:
        if maze[i+x][j+y] == 'o' and visited[i+x][j+y] == False:
          stack.push( (i+x, j+y) )
          visited[i+x][j+y] = True
          
  return False



maze = ['oxxxx', 
        'ooooo',
        'xxxxo',
        'xxxxo']

maze2 = ['oxxxx', 
        'ooooo',
        'xxxxx',
        'xxxxo']



#use doublelinked list 
