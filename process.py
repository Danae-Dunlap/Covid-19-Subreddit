class Process(): 
  subreddit_data = []
  users = []
  posts = []
  
  def __init__(self, file_name): 
    self.file_name = file_name

  """Gathers the data from the file that specifically focuses on the comments into a list(subreddit_data)."""
  def createData(self): 
    
    with open ('{}'.format(self.file_name)) as file: 
     for line in file:
        self.subreddit_data.append(line.strip('\n'))
       
    self.subreddit_data = self.subreddit_data[self.subreddit_data.index('level 1'):self.subreddit_data.index("Subreddit Icon", self.subreddit_data.index('level 1') + 1) - 1]
  
    return self.subreddit_data
  
  """Puts the usernames of everyone who commmented on the subreddit into a list (users)."""
  def findUsers(self):
    subreddit_data = self.createData()
    self.users = []
    #Puts the information about usernames and post into the aforementioned lists
    for i in range(len(subreddit_data)): 
      if 'level' in subreddit_data[i] and 'Reply' not in subreddit_data[i+1]: 
        self.users.append(subreddit_data[i+1])

    return self.users    
    
  """Puts the actual comments from the subreddit into a list (posts). """
  def findPosts(self):
    subreddit_data = self.createData()
    posts = []
    for i in range(len(subreddit_data)): 
      if 'ago' in subreddit_data[i] and 'edited' not in subreddit_data[i+1]: 
        posts.append(subreddit_data[i+1:subreddit_data.index("Reply", i)])
    return posts
      
  """"Prints the numbers of users that have posted in the subreddit and the names of those that have posted more than once. """
  def taskAB(self): 
    users = self.findUsers()
    more_than_once = set()
    for user in users: 
      if users.count(user) > 1: 
        more_than_once.add(user)
        
    #Task A) Prints the number of users that have posted onto the reddit
    print(str(len(user)) + " users have posted to the subreddit.")
    
    #Task B) Prints the usernames of everyone who posted more than once
    print("The following users have posted more than once:")
    for name in more_than_once: 
      print(name)

  """Completes Task C from Task 1: Prints the post that have metion cough, fever, and/or cold."""
  def taskC(self): 
    #Checks for the post that contain the key words and puts them into the sick list
    posts = self.findPosts()
    sick = []
    symptomps = ["cough", "cold", "fever" ]
    
    for i in range(len(posts)): 
      for symptomp in symptomps: 
        if symptomp in ''.join(posts[i]).lower(): 
          sick.append(''.join(posts[i]))
          continue
  
    #Task C) Prints the post that have the mentioned symptoms in them
    print("The following post contain the mention of coughing, cold, and/or fever")
    for post in sick: 
      print(post)

    return sick
      
  """Used to run all of the tasks at once"""
  def run(self):  
    self.taskAB()
    self.taskC()

