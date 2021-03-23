"""
Class Inheritance
"""
# Defining Class
class Team:
    def __init__(self,Name="Name",Origin="Origin"): # if Values are not given for name and origin then show default
        self.TeamName = Name
        self.TeamOrigin = Origin

    def DefiningTeamName(self,Name):
        self.TeamName= Name

    def DefiningTeamOrigin(self, Origin):
        self.TeamOrigin = Origin

class Player(Team): # in parenthesis parent class
    def __init__(self,PlayerName,PPoints,TeamName,TeamOrigin):
        Team.__init__(self,TeamName,TeamOrigin) # Passing Attributes values to Parent class
        self.PlayerName = PlayerName
        self.PlayerPoint = PPoints

    def ScoredPoint(self):
        self.PlayerPoint += 1

    def setName(self,Name):
        self.PlayerName = Name

    def __str__(self):
        return self.PlayerName + " has scord: " + str(self.PlayerPoint) + " Points"

Player1 = Player("Sid",0,"Sharks","Chicago")
print(Player1.PlayerName)
print(Player1.PlayerPoint)
# Player1.DefiningTeamName("Sharks")
print(Player1.TeamName) # Accessing Attributes of parents class
print(Player1.TeamOrigin)

Player1.ScoredPoint()
print(Player1.PlayerPoint)

Player1.setName("Lee")
print(Player1.PlayerName)

print(Player1)

# Team1=Team("Tigier","Chicago")
#
# Team2 = Team("Hawks","New York")
#
# Team3 = Team()
# print("Default name is:",Team1.TeamName) # printing values of class's variable
# print("Defalult Origin is:",Team1.TeamOrigin)
# NameT1 = input("\nEnter team 1 name: ")
# OriginT1 = input("Enter team 1 origin: ")
#
# NameT2 = input("\nEnter team 2 name: ")
# OriginT2 = input("Enter team 2 origin: ")
#
# NameT3 = input("\nEnter team 3 name: ")
# OriginT3 = input("Enter team 3 origin: ")
#
# Team1.DefiningTeamName(NameT1) # Assigning value to the class variable / Calling function which is inside class
# Team1.DefiningTeamOrigin(OriginT1)
# print("\nTeam name 1 is:", Team1.TeamName)
# print("Team 1 Origin is:",Team1.TeamOrigin)
#
# Team2.DefiningTeamName(NameT2)
# Team2.DefiningTeamOrigin(OriginT2)
# print("\nTeam 2 name:",Team2.TeamName)
# print("Team 2 Origin ",Team2.TeamOrigin)
#
# Team3.DefiningTeamName(NameT3)
# Team3.DefiningTeamOrigin(OriginT3)
# print("\nTeam 3 name:",Team3.TeamName)
# print("Team 3 name:",Team3.TeamOrigin)

