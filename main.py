import os
os.system('pip install scratchconnect')
while True:
  import scratchconnect

  login = scratchconnect.ScratchConnect('Username', 'Password')
  user = login.connect_user(username="ANYUSER")

  latestcomment = str(user.comments(limit=1, page=1))

  partitioned_string = latestcomment.partition("'User': '")
  partone = partitioned_string[2]
  parttwo = partone.partition("',")
  commenter = parttwo[0]

  print(commenter)
  login.follow_user(username=str(commenter))
