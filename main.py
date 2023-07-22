def find_famous_cat(cats):
  name = []
  followers = []
  famous = []
  
  for cat in cats:
    name.append(cat["name"])
    followers.append(sum(cat["followers"]))

  for i, value in enumerate(followers, 0): 
    if value == max(followers):
      famous.append(name[i])

  return famous  

response = find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
])

print(response)
  
  