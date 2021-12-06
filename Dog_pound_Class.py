import random, time, datetime #importing moduels 
#used textbook for module informationdadadad
class Dog():
    personality = "Good Dog!" #something that applies to all dogs (Class Variable)

    #constructor
    def __init__(self, name, size, breed):
       self.__name = name #sets he name
       self.__size = size #set size must be try except, raise,
       self.__breed = breed #sets the breed

    def set_name(self,name): #defines set name variable
       #setting name
       self.__name = name #sets name
 
    def get_name(self): #defines get name variable
       #returning name
       return self.__name #returns self name
  
    def set_size(self,size): #defines set size
       #setting size
       self.__size = size #sets size
  
    def get_size(self): #gets size
       #return size
       return self.__size

    def set_breed(self,breed): #define breed
        #setting breed
        self.__breed = breed
      
    def get_breed(self): #gets breed 
        #return breed
        return self.__breed

    def personality1(self,breed): #define personalities for dog that takes in the variable breed
        #These are list of attributes for each type of breed available
        Huskyp = ["is outgoing and friendly with people", "is very social with other dogs and plays alot", "loves to run around for hours and enjoys walks"]
        GoldenRetrieverp = ["loves to play and eat alot of food", "is very quiet most of the day and likes to take walks", 'eats alot of food, but runs alot and enjoys playing inside']
        Pitbullp =["is protective of other dogs and people", "chases alot of squirrels and loves to be pet", "is very social with other dogs and likes to bath"]
        Poodlep =['only eats fancy meals and loves to play','can do alot of tricks and loves to go for walks','loves to be cleaned and very social with other dogs']
        GermanShepardp = ['howls at the moon with other dogs and sleeps during the day', 'is very loyal to a lot of the dog handlers here and can run for a long time', 'is well behaved and has never shown agression']
        Chihuahuap = ['barks at any threat and loves to play with other dogs','is family oriented and loves to eat','can run super fast. I think this is the fastest chiuahua here']
        Pugp = ['is quiet most of the times except when playing and understands alot of commands','loves to wag their tail and roll over','is very great to take places and doesnt bark in car rides']
        ShibaInup = ['loves to take pictures and to be around crowds','likes to keep fur away from water and does not like dry food', 'loves to be fed and takes naps all through out the day']
        Dalmationp = ['is playful and loves to jump around','will bark any time the name Cruella is mentioned and will like to play fetch','can do alot of tricks and is family oriented']
        #if statements that return a ramdom attribute for the given breed from list. I use random.choice to get only 1
        if breed == "Husky":
            a = random.choice(Huskyp)
            return(a)
        if breed == "Golden Retriever":
            b = random.choice(GoldenRetrieverp)
            return(b)
        if breed == "Pitbull":
            c = random.choice(Pitbullp)
            return(c)
        if breed == "Poodle":
            d = random.choice(Poodlep)
            return(d)
        if breed == "German Shepard":
            e = random.choice(GermanShepardp)
            return(e)
        if breed == "Chihuahua":
            f = random.choice(Chihuahuap)
            return(f)
        if breed == "Pug":
            g = random.choice(Pugp)
            return(g)
        if breed == "Shiba Inu":
            h = random.choice(ShibaInup)
            return(h)
        if breed == "Dalmation":
            i = random.choice(Dalmationp)
            return(i)
        #end of if statements that give breeds certain attributes

    def age(self,size,breed): #define age for the dog
        Age1 = [" puppy", " teen"] #list that only has puppy teen
        Age2 = [" teen", 'n adult'] #age has teen and adult
        Age3 = [' puppy',' teen','n adult'] #age 3 has all ages
        #if statements that determine age for each dog based on breed and size
        if breed == "Chihuahua" and size == "small":
            Age = random.choice(Age3) #sets age to a random choice from specific list an d
            return(Age)
        if breed == "Pug" and size == "small":
            Age = random.choice(Age3)
            return(Age)
        elif size == "small":
            Age = random.choice(Age1)
            return(Age)
        elif size == "medium" or "large":
            Age = random.choice(Age2)
            return(Age)
        #end of if statements

def picture_of_dog(): #define picture of dog
            #returns pixel art of dog
            print(",-.___,-.")
            print("\_/_ _\_/")        
            print("  )O_O(  ")  
            print(" { (_) } ")                      
            print("  `-^-'  ")

def loading():#define loading
    #this is a loading animation usign time and sleep to loading arrows at specific points
    print("--->",end=" ")
    print("--->", end=" ")
    time.sleep(.2) #timers per second
    print("--->", end=" ")
    time.sleep(.3)
    print("--->", end=" ")
    time.sleep(.4)
    print("--->", end=" ")
    time.sleep(.5)

def main(): #main program which is the demo program
    #this program uses get set methods and other methods to get user inputs to choose right dog for adoption
    #Demo Program Adoption Center using class!
    Adopted_Dog = Dog #set the dog class to a variable
    Available_breeds = ("Husky", "Golden Retriever", "Pitbull", "Poodle", "German Shepard", "Chihuahua", "Pug", "Shiba Inu", "Dalmation") #all breeds in adoption center
    print("Hello Welcome To Your Local Dog Adoption Center!!!"'\n') #greeting
    time.sleep(1) #lets user read 
    #loop to check if user wants to adopt available animals if not, it will give more!
    while True: #while loop
        Todays_selection0 = random.sample(Available_breeds,k=5) #gets random breed 5
        Todays_selection = (', '.join(Todays_selection0)) #prints those breeds
        print(f"We have 5 breeds of dogs available for adpotion today which are: {Todays_selection}!"'\n') #greeting
        time.sleep(1.7) #time to read
        breed = input("Which breed of dog are you interested in from our selection today? If none say 'none': ") #inputs which breed user
        breed = breed.title() #formats answer
        if breed in Todays_selection0: #checks if its a valid response
            Adopted_Dog.set_breed(Dog,breed) #sets breed to the chosen breed
            break #breaks out
        if breed == "None": #if user doesnt want to then it will loop them into choosing one they want
            print(" ") #spacer
            print("Sorry to hear that! Come again tommorow!"'\n') #greeting
            animation_arrow = loading() #loading animation
            (animation_arrow)
            print("A Day Passes",end = "") #greeting
            loading() #loading animation
            print("Welcome Back!""\n") #loading animation
        else: #if statement
            print(" ")
            print("Sorry but that breed is not available today, please choose again or say 'none'!"'\n') #greeting
            continue #loops

    chosen_breed = Adopted_Dog.get_breed(Dog) #sets chosen breed using get set method
    print(" ") #formating
    print(f"Great choice to look at a {chosen_breed} today, let me show you the way!"'\n') #greeting
    animation_arrow = loading() #loading
    (animation_arrow)
    print(" Great we are here!"'\n') #greeting

    #allows the user to choose size. This will affect the age
    while True: #whole loop
        time.sleep(1) #allows load
        size = input(f"We have many {chosen_breed}'s to choose from today. Are you interested in a small, medium, or large {chosen_breed}?: ") #input for wanted size
        size = size.lower() #lower case the answer
        print("") #formatiing
        #if statements that set the size of the dog given the users answers
        if size == "small":
            print('Good choice! Small dogs are so cute!''\n')
            Adopted_Dog.set_size(Dog,size)
            break
        if size == "medium":
            print('Good choice! Medium sized dogs are great for the house!''\n')
            Adopted_Dog.set_size(Dog,size)
            break
        if size == "large":
            print('Good choice! Large dogs are great for outdoors activities!''\n')
            Adopted_Dog.set_size(Dog,size)
            break 
        else: 
            print("Sorry we do not have that size!"'\n')   
            continue #loops
        #end of choosing size
    time.sleep(1)   #time to read
    dog_names = ["Dash", "Sally", "Clifford", "Diego", "Rex", "Blue", "Pika", "Layla", "Jin Boo", "Sarku", "Max",] #basic names
    chosen_size = Adopted_Dog.get_size(Dog) #sets size
    while True: #while loop
        name = random.choice(dog_names) #random name for the dog
        print(f"Here is {name}, who is a {chosen_size} {chosen_breed}.",end=" ") #uses variables to correctly set new dog each time
        print(f"{name}", end=" ") #name
        print(f"{Adopted_Dog.personality1(Dog,breed)}.", end= " ") #uses personality method
        print(f"{name} is a{Adopted_Dog.age(Dog,size,breed)}."'\n') #gives dog

        choice1 = input(f"Do you want to adopt {name}. They are very fond of you! ('yes' or 'no'): ") #choice of adoption
        choice1.lower() #formats choice
        if choice1 == "yes": #breaks if yes
            break
        else: #if no then it will loop to find right dog
            print(" ")
            print("Thats ok, lets look again!"'\n')
            continue #loops
    print(" ") #formating
    print(f"Congratulations on adopting {name}! It is now time to fill out adoption papers!""\n") #greeting
    resetname = input(f"Would you like to rename {name}? ('yes' or 'no'): ") #input to rename dog will use set method
    resetname.lower()#formats lower
    if resetname == "yes": #if yes new name will be given
        print(" ")
        new_name = input("Enter a new name: ") #inputs name
        Adopted_Dog.set_name(Dog,new_name) #sets name
    if resetname == "no": #will use basic name
        Adopted_Dog.set_name(Dog,name)
    print(" ") #formating
    chosen_name = Adopted_Dog.get_name(Dog) #gives name using get set method
    owner_name = input("Sign here to adopt: ") #input gets signature
    print(" ") #formating
    print("Great, give me a few minutes while I get your adoption certificate!""\n") #greeting
    loading() #loading animation
    print(" ""\n") #new line
    date = datetime.datetime.now() #gets the exact date for adoption form using datetime module
    #prints adoption form
    print("_________________________________""\n") #line for formating
    print("Adoption Date: ", end = " ") #date
    print(date.strftime("%m-%d-%y"),"\n") #sets the date in order month day and year
    print(f"Name of dog: {chosen_name}""\n") #get name
    print(f"Breed of dog: {chosen_breed}""\n") #get breed
    print(f"Size: {chosen_size}""\n") #get size
    picture_of_dog() #gives picture of dog
    print(" ") #spacing
    print(f"Owners Signature: X___{owner_name}____""\n") #owner signature
    print("_________________________________""\n") #formating
    print(f"Enjoy your new pet! {chosen_name} is a {Adopted_Dog.personality}") #class variable!
    print("Thank You!") #thanking user
    #end of demo program
if __name__ == "__main__":#calls main function
    main()