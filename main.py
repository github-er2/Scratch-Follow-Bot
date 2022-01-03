while{} True:
  import os

  os.system('pip install scratchconnect')

  import scratchconnect

  login = scratchconnect.ScratchConnect('thebesttestoutthere', ' =D')

  project = login.connect_project(project_id=603845519,
                              access_unshared=False)

  latestcomment = str(project.comments(all=False, limit=1, offset=0, comment_id=None))

  partitioned_string = latestcomment.partition("'username': '")
  partone = partitioned_string[2]
  parttwo = partone.partition("',")
  commenter = parttwo[0]

  print(commenter)
  login.follow_user(username=str(commenter))
