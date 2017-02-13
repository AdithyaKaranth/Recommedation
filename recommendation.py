#refer guidetodatamining.com for more details
from math import sqrt
def manhattan(user1,user2):
  distance=0
  for user in user1:#name of the bands
    if user in user2:#computes only if the band is present
      distance+=abs(user1[user]-user2[user])#formula for manhattan distance
  return distance

def pearson(user1,user2):
  sum_xy=0
  sum_x=0
  sum_y=0
  sum_x2=0
  sum_y2=0
  n=0
  for user in user1:
    if user in user2:
      n=n+1
      sum_xy+=user1[user]*user2[user]
      sum_x+=user1[user]
      sum_y+=user2[user]
      sum_x2+=user1[user]**2
      sum_y2+=user2[user]**2
  if n==0:
    return 0
  denom=sqrt((sum_x2-(sum_x**2)/n)*(sum_y2-(sum_y**2)/n))
  if denom == 0:
    return 0
  return (sum_xy-(sum_x*sum_y)/n)/denom

def cosine(user1,user2):
  sum_xy=0
  sum_x2=0
  sum_y2=0
  for user in user1:
     if user in user2:
        sum_xy+=user1[user]*user2[user]
     sum_x2+=user1[user]**2
  for user in user2:
    sum_y2+=user2[user]**2
  return sum_xy/(sqrt(sum_x2*sum_y2))
def NearestNeighbour(users,username):
  distance=[]
  for user in users:
    dist=0
    if user != username: 
       dist=manhattan(users[user],users[username])
       distance.append((dist,user))
  distance.sort()
  #print distance[0]
  return distance

def recommend(users,username):
  neighbour=NearestNeighbour(users,username)[0][1]
  nearest=users[neighbour]
  user=users[username]
  recommend=[]
  for artist in nearest:
    if not artist in user:
      recommend.append((nearest[artist],artist))
  print recommend
  


users={"Angelica":{"Blues Traveler":3.5,"Broken Bells":2,"Norah Jones":4.5,
	"Phoenix":5,"Slightly Stoopid":1.5,"The Strokes":2.5,"Vampire Weekend":2},
"Bill":{"Blues Traveler":2,"Broken Bells":3.5,"Deadmau5":4,"Phoenix":2,"Slightly Stoopid":3.5,"Vampire Weekend":3},
"Chan":{"Blues Traveler":5,"Broken Bells":1,"Deadmau5":1,"Norah Jones":3,"Phoenix":5,"Slightly Stoopid":1,},
"Dan":{"Blues Traveler":3,"Broken Bells":4,"Deadmau5":4.5,"Phoenix":3,"Slightly Stoopid":4.5,"The Strokes":4,"Vampire Weekend":2},
"Hailey":{"Broken Bells":4,"Deadmau5":1,"Norah Jones":4,"The Strokes":4,"Vampire Weekend":1},
"Jordyn":{"Broken Bells":4.5,"Deadmau5":4,"Norah Jones":5,"Phoenix":5,"Slightly Stoopid":4.5,"The Strokes":4,"Vampire Weekend":4},
"Sam":{"Blues Traveler":5,"Broken Bells":2,"Norah Jones":3,"Phoenix":5,"Slightly Stoopid":4,"The Strokes":5},
"Veronica":{"Blues Traveler":3,"Norah Jones":5,"Phoenix":4,"Slightly Stoopid":2.5,"The Strokes":3}}


#print NearestNeighbour(users,"Hailey")can't use users["Hailey"].check later(list compare)
#recommend(users,"Angelica")
#print pearson(users["Angelica"],users["Bill"])
#print pearson(users["Angelica"],users["Hailey"])
#print pearson(users["Angelica"],users["Jordyn"])

print cosine(users["Angelica"],users["Veronica"])
