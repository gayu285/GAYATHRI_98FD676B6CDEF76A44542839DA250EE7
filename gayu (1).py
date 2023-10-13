'''Implement a class called player that represent a cricket player.The player class should have  a method called play{} which prints "The player is playing cricket.Derive two classes,Batsman and Bowler,from the player class.Override the play() method in each derived class to print "The batsman is batting " and "The bowler is  bowling",respectively.write a program to Create  objects of both the Batsman and Bowler classes and call the play() method for each objects.''' 


#Difine the base class player 
class player:

  def play(self):
    print("The player is playing cricket.")


#Define the derived class Batsman
class Batsman(player):

  def play(self):
    print("The bowler is bowling.")


#Define the derived class Bowler
class Bowler(player):

  def play(self):
    print("The bowler is bowler.")


#Create objects of Betsman and Bowler classes 
batsman = Batsman()
bowler = Bowler()
#call the play() method for each object 
batsman.play()
bowler.play()