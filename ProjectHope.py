# Project hope...
#imports the needed libraries and file for the program
import numpy as N
from random import randint
Archerloc = N.loadtxt('Workbook1.csv', delimiter=',',skiprows=1)
from geopy.geocoders import GoogleV3
from geopy.distance import vincenty
geolocator = GoogleV3()

# distance takes 2 variables, current location and archers location, and calculates the distance between the two
def distance(X,Y):
	dist = vincenty(X, Y)
	return dist
#Direction takes 2 variables, current location and archers location, and calculates the direction archer is from the current location
def direction(X,Y):
	if X[0] < Y[0] and X[1] > Y[1]:
		direction = "North East"
		
	if X[0] < Y[0] and X[1] < Y[1]:
		direction = "North West"
		
	if X[0] > Y[0] and X[1] > Y[1]:
		direction = "South West"
		
	if X[0] > Y[0] and X[1] < Y[1]:
		direction = "South East"
	if X[0] == Y[0] and X[1] == Y[1]:
		direction = '0'
		
	return direction

# JFK, Honolulu, Miami, New Orleans, Parris, and Russia are all major locations.  Arhcer's location can be found from these locations, or other major locations my be accessed. 
#JFK contains all the locations and their information, Distance and direction, that one can access from JFK, as well as the same for archers location 
def JFK(NS,DZ):
	C = distance(NS,DZ) #Distance to archer
	D = direction(NS,DZ) #Direction to archer 
	hono = Archerloc[5,0],Archerloc[5,1] #cord of Hono airport
	HD = distance(NS,hono)
	HD1 = direction(NS,hono)
	mi = Archerloc[6,0],Archerloc[6,1]
	MD = distance(NS,mi)
	MD1 = direction(NS,mi)
	no= Archerloc[7,0],Archerloc[7,1]
	NOD = distance(NS,no)
	NOD1 = direction(NS,no)
	par = Archerloc[8,0],Archerloc[8,1]
	PD = distance(NS,par)
	PD1 = direction(NS,par)
	rus = Archerloc[9,0],Archerloc[9,1]
	RD = distance(NS,rus)
	RD1 = direction(NS,rus)
	print ''
	print 'You are in New York'
	print "Archers location is", C, D,'of your current location...'
	print "These are the locations you can travel from your current location:"
	print ''
	print '1. Honolulu is', HD,'to the', HD1
	print '2. Miami is', MD,'to the', MD1
	print '3. New Orleans  is', NOD,'to the', NOD1
	print '4. Parris is', PD,'to the', PD1
	print '5. Moscow is', RD,'to the', RD1
	print '6. Quit'
	S = raw_input('please make your selection: ')
	if S == '1':
		NS = hono
		DZ = DZ
		Next = honolulu(NS,DZ)
		return N
	if S == '2':
		NS = mi
		DZ = DZ
		Next = miami(NS,DZ)
	if S == '3':
		NS = no
		DZ = DZ
		Next = NewOrleans(NS,DZ)
	if S == '4':
		NS = par
		DZ = DZ
		Next = parris(NS,DZ)
	if S == '5':
		NS = rus
		DZ = DZ
		Next = russia(NS,DZ)
	if S == '6':
		print 'Good-Bye'
		exit
		
#Honolulu contains all the locations and their information, Distance and direction, that one can access from Honolulu, as well as the same for archers location 	
def honolulu(NS,DZ):
	C = distance(NS,DZ)
	D = direction(NS,DZ)
	ti = Archerloc[10,0],Archerloc[10,1]
	TID = distance(NS,ti)
	TID1 = direction(NS,ti)
	ny = Archerloc[1,0],Archerloc[1,1]
	NYD = distance(NS,ny)
	NYD1 = direction(NS,ny)
	no= Archerloc[7,0],Archerloc[7,1]
	NOD = distance(NS,no)
	NOD1 = direction(NS,no)
	rus = Archerloc[9,0],Archerloc[9,1]
	RD = distance(NS,rus)
	RD1 = direction(NS,rus)
	print ''
	print 'You are in Honolulu'
	print "Archers location is", C, D,'of your current location...'
	print "These are the locations you can travel from your current location:"
	print ''
	print '1. JFK is', NYD, 'to the', NYD1
	print '2. Tahihi is', TID, 'to the', TID1
	print '3. New Orleans is', NOD,'to the', NOD1
	print '4. Moscow is', RD,'to the', RD1
	print '5. Quit'
	print ''
	S = raw_input('please make your selection: ')
	if S == '1':
		NS = ny
		DZ = DZ
		Next = JFK(NS,DZ)
	if S == '2':
		NS = ti
		DZ = DZ
		Next = tahiti(NS,DZ)
	if S == '3':
		NS = no
		DZ = DZ
		Next = NewOrleans(NS,DZ)
	if S == '4':
		NS = rus
		DZ = DZ
		Next = russia(NS,DZ)
	if S == '5':
		print 'Good-Bye'
		exit		
		
#Miami contains all the locations and their information, Distance and direction, that one can access from Miami, as well as the same for archers location 		
def miami(NS,DZ):
	C = distance(NS,DZ)
	D = direction(NS,DZ)
	ny = Archerloc[1,0],Archerloc[1,1]
	NYD = distance(NS,ny)
	NYD1 = direction(NS,ny)
	sb = Archerloc[11,0],Archerloc[11,1]
	SBD = distance(NS,sb)
	SBD1 = direction(NS,sb)
	no= Archerloc[7,0],Archerloc[7,1]
	NOD = distance(NS,no)
	NOD1 = direction(NS,no)
	print ''
	print 'You are in Miami'
	print "Archers location is", C, D,'of your current location...'
	print "These are the locations you can travel from your current location:"
	print ''
	print '1. JFK is', NYD, 'to the', NYD1
	print '2. South Beach is', SBD, 'to the', SBD1
	print '3. New Orleans is', NOD,'to the', NOD1
	print '4. Quit'
	print ''
	S = raw_input('please make your selection: ')
	if S == '1':
		NS = ny
		DZ = DZ
		Next = JFK(NS,DZ)
	if S == '2':
		NS = sb
		DZ = DZ
		Next = southbeach(NS,DZ)
	if S == '3':
		NS = no
		DZ = DZ
		Next = NewOrleans(NS,DZ)
	if S == '4':
		print 'Good-Bye'
		exit
		
#New Orleans contains all the locations and their information, Distance and direction, that one can access from New Orleans, as well as the same for archers location 
def NewOrleans(NS,DZ):
	C = distance(NS,DZ)
	D = direction(NS,DZ)
	ny = Archerloc[1,0],Archerloc[1,1]
	NYD = distance(NS,ny)
	NYD1 = direction(NS,ny)
	hono = Archerloc[5,0],Archerloc[5,1] #cord of Hono airport
	HD = distance(NS,hono)
	HD1 = direction(NS,hono)
	mi = Archerloc[6,0],Archerloc[6,1]
	MD = distance(NS,mi)
	MD1 = direction(NS,mi)
	swp = Archerloc[12,0],Archerloc[12,1]
	SWD = distance(NS,swp)
	SWD1 = direction(NS,swp)
	print ''
	print 'You are in New Orleans'
	print "Archers location is", C, D,'of your current location...'
	print "These are the locations you can travel from your current location:"
	print ''
	print '1. JFK is', NYD, 'to the', NYD1
	print '2. Honolulu is', HD,'to the', HD1
	print '3. Miami is', MD,'to the', MD1
	print '4. The Swamp is', SWD, 'to the', SWD1
	print '5. Quit'
	print ''
	S = raw_input('please make your selection: ')
	if S == '1':
		NS = ny
		DZ = DZ
		Next = JFK(NS,DZ)
	if S == '2':
		NS = hono
		DZ = DZ
		Next = honolulu(NS,DZ)
	if S == '3':
		NS = mi
		DZ = DZ
		Next = miami(NS,DZ)
	if S == '4':
		NS = swp
		DZ = DZ
		Next = swamp(NS,DZ)
	
	if S == '5':
		print 'Good-Bye'
		exit
		
#Parris contains all the locations and their information, Distance and direction, that one can access from Parris, as well as the same for archers location 		
def parris(NS,DZ):
	C = distance(NS,DZ)
	D = direction(NS,DZ)
	GS = Archerloc[13,0],Archerloc[13,1]
	GSD = distance(NS,GS)
	GSD1 = direction(NS,GS)
	ny = Archerloc[1,0],Archerloc[1,1]
	NYD = distance(NS,ny)
	NYD1 = direction(NS,ny)
	mi = Archerloc[6,0],Archerloc[6,1]
	MD = distance(NS,mi)
	MD1 = direction(NS,mi)
	rus = Archerloc[9,0],Archerloc[9,1]
	RD = distance(NS,rus)
	RD1 = direction(NS,rus)
	print ''
	print 'You are in Parris'
	print "Archers location is", C, D,'of your current location...'
	print "These are the locations you can travel from your current location:"
	print ''
	print '1. JFK is', NYD, 'to the', NYD1
	print '2. Miami is', MD, 'to the', MD1
	print '3. Gstaasd is', GSD,'to the', GSD1
	print '4. Moscow is', RD,'to the', RD1
	print '5. Quit'
	print ''
	S = raw_input('please make your selection: ')
	if S == '1':
		NS = ny
		DZ = DZ
		Next = JFK(NS,DZ)
	if S == '2':
		NS = mi
		DZ = DZ
		Next = miami(NS,DZ)
	if S == '3':
		NS = GS
		DZ = DZ
		Next = gstaad(NS,DZ)
	if S == '4':
		NS = rus
		DZ = DZ
		Next = russia(NS,DZ)
	if S == '5':
		print 'Good-Bye'
		exit		
		
#Russia contains all the locations and their information, Distance and direction, that one can access from Russia, as well as the same for archers location 
def russia(NS,DZ):
	C = distance(NS,DZ)
	D = direction(NS,DZ)
	vy = Archerloc[10,0],Archerloc[10,1]
	VD = distance(NS,vy)
	VD1 = direction(NS,vy)
	ny = Archerloc[1,0],Archerloc[1,1]
	NYD = distance(NS,ny)
	NYD1 = direction(NS,ny)
	par = Archerloc[8,0],Archerloc[8,1]
	PD = distance(NS,par)
	PD1 = direction(NS,par)
	hono = Archerloc[5,0],Archerloc[5,1] #cord of Hono airport
	HD = distance(NS,hono)
	HD1 = direction(NS,hono)
	
	print ''
	print 'You are in Moscow'
	print "Archers location is", C, D,'of your current location...'
	print "These are the locations you can travel from your current location:"
	print ''
	print '1. JFK is', NYD, 'to the', NYD1
	print '2. Parris is', PD, 'to the', PD1
	print '3. Vyborg is', VD,'to the', VD1
	print '4. Honolulu  is', HD,'to the', HD1
	print '5. Quit'
	print ''
	S = raw_input('please make your selection: ')
	if S == '1':
		NS = ny
		DZ = DZ
		Next = JFK(NS,DZ)
	if S == '2':
		NS = par
		DZ = DZ
		Next = parris(NS,DZ)
	if S == '3':
		NS = vy
		DZ = DZ
		Next = vyborg(NS,DZ)
	if S == '4':
		NS = hono
		DZ = DZ
		Next = honolulu(NS,DZ)
	if S == '4':
		print 'Good-Bye'
		exit	

# These are the smaller locations archer might be hiding.  The contain a method of checking to see if archer is there, as well as allowing the user to play again if they find him, go back to a major airport, or quit		

def tahiti(NS,DZ):
	Q = distance(DZ,NS)
	P = direction(DZ,NS)
	hono = Archerloc[5,0],Archerloc[5,1] #cord of Hono airport
	HD = distance(NS,hono)
	HD1 = direction(NS,hono)
	if Q == 0:
		print ''
		print 'You found Archer in Tahiti!!!'
		print ''
		S = raw_input('Play again? y/n')
		if S =='y':
			R = (randint(0,4))
			E = travel(R)
		else:
			print 'Good-Bye'
			exit
			
	else:
		print 'You are in Tahiti'
		print "Archers location is", Q, P,'of your current location...'
		print "These are the locations you can travel from your current location:"
		print '1. Honolulu is', HD,'to the', HD1
		print '2. Quit'
		S = raw_input('please make your selection: ')
		if S == '1':
			NS = hono
			DZ = DZ
			Next = honolulu(NS,DZ)
		if S == '2':
			print 'Good-Bye'
			exit
def southbeach(NS,DZ):
	Q = distance(DZ,NS)
	P = direction(DZ,NS)
	mi = Archerloc[6,0],Archerloc[6,1]
	MD = distance(NS,mi)
	MD1 = direction(NS,mi)
	if Q == 0:
		print ''
		print 'You found Archer in South Beach!!!'
		print ''
		S = raw_input('Play again? y/n')
		if S =='y':
			R = (randint(0,4))
			E = travel(R)
		else:
			print 'Good-Bye'
			exit
	else:
		print 'You are in South Beach'
		print "Archers location is", Q, P,'of your current location...'
		print "These are the locations you can travel from your current location:"
		print '1. Miami is', MD,'to the', MD1
		print '2. Quit'
		S = raw_input('please make your selection: ')
		if S == '1':
			NS = mi
			DZ = DZ
			Next = miami(NS,DZ)
		if S == '2':
			print 'Good-Bye'
			exit		
def swamp(NS,DZ):
	Q = distance(DZ,NS)
	P = direction(DZ,NS)
	no= Archerloc[7,0],Archerloc[7,1]
	NOD = distance(NS,no)
	NOD1 = direction(NS,no)
	if Q == 0:
		print ''
		print 'You found Archer in the Swamp!!!'
		print ''
		S = raw_input('Play again? y/n')
		if S =='y':
			R = (randint(0,4))
			E = travel(R)
		else:
			print 'Good-Bye'
			exit
	else:
		print 'You are in the Swamp'
		print "Archers location is", Q, P,'of your current location...'
		print "These are the locations you can travel from your current location:"
		print '1. New Orleans is', NOD,'to the', NOD1
		print '2. Quit'
		S = raw_input('please make your selection: ')
		if S == '1':
			NS = hono
			DZ = DZ
			Next = honolulu(NS,DZ)
		if S == '2':
			print 'Good-Bye'
			exit
def gstaad(NS,DZ):
	Q = distance(DZ,NS)
	P = direction(DZ,NS)
	par = Archerloc[8,0],Archerloc[8,1]
	PD = distance(NS,par)
	PD1 = direction(NS,par)
	if Q == 0:
		print ''
		print 'You found Archer in Gstaad!!!'
		print ''
		S = raw_input('Play again? y/n')
		if S =='y':
			R = (randint(0,4))
			E = travel(R)
		else:
			print 'Good-Bye'
			exit
	else:
		print 'You are in Gstaad'
		print "Archers location is", Q, P,'of your current location...'
		print "These are the locations you can travel from your current location:"
		print '1. Parris is', PD,'to the', PD1
		print '2. Quit'
		S = raw_input('please make your selection: ')
		if S == '1':
			NS = par
			DZ = DZ
			Next = parris(NS,DZ)
		if S == '2':
			print 'Good-Bye'
			exit
def vybork(Ns,DZ):
	Q = distance(DZ,NS)
	P = direction(DZ,NS)
	rus = Archerloc[9,0],Archerloc[9,1]
	RD = distance(NS,rus)
	RD1 = direction(NS,rus)
	if Q == 0:
		print ''
		print 'You found Archer in Vyborg!!!'
		print ''
		S = raw_input('Play again? y/n')
		if S =='y':
			R = (randint(0,4))
			E = travel(R)
		else:
			print 'Good-Bye'
			exit
	else:
		print 'You are in Vyborg'
		print "Archers location is", Q, P,'of your current location...'
		print "These are the locations you can travel from your current location:"
		print '1. Moscow is', PD,'to the', PD1
		print '2. Quit'
		S = raw_input('please make your selection: ')
		if S == '1':
			NS = rus
			DZ = DZ
			Next = russia(NS,DZ)
		if S == '2':
			print 'Good-Bye'
			exit
	
# Travel is where a random int is used to determine where archer is missing.  In my list these areas start after position 10 on the list, hence the Z+10.  The Spreadsheet is organized as a 2 by 15 array. Archerloc[Z,0] represents the latitude, and Archerloc[Z,1] represents the longitude.
def travel(R):
	Z = R + 0
	NS = Archerloc[Z,0], Archerloc[Z,1] #Home GPS
	DZ = Archerloc[Z+10,0], Archerloc[Z+10,1]
	start = JFK(NS,DZ)
	return start
	
	
	
#Opening is just the text opening that is displayed in the very beginning	
def opening():
	print ''
	print ''
	print 'Agent Sterling Archer, codename Duchess.'
	print 'Licensed to kill.'
	print 'Primary skills: covert operations.'
	print 'Unarmed combat.'
	print 'Firearms.'
	print 'Explosives.'
	print 'Asset acquisition.'
	print 'Enemy agent disposal.'
	print 'Current status: missing...'
	print ''
	print ''
	
# Main doesnt provide much in the program. It ask the user if they want to play and then gets the random int that is then passed to the function travel where it is used to assign a location for the missing archer.			
def main():
	print 'Welcome to Where in the World is Archer!'
	print ''
	run = input('Would you like to play?? (y=1/n=2)')
	if run == 1:
		A = opening()
		R = (randint(0,4))
		E = travel(R)
	else:
		print "Good Bye"
main()
