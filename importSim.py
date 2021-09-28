class Room:
    def __init__(self, name): 
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
        
    def __repr__(self): 
        return "Room(name: {})".format(self.name)

class Task:
    def __init__(self, name, isCompleted = False):
        self.name = name
        self.isCompleted = isCompleted

    def __eq__(self, other):
        return (self.name, self.isCompleted) == (other.name, other.isCompleted)

    def __repr__(self):
        return "Task(name: {}, isCompleted: {})".format(self.name, self.isCompleted)

class Crewmate:
    def __init__(self, n, c, ac = ()):
        self.name = n
        self.color = c
        self.accessories = ac
        self.isAlive = True
        self.tasksDone = 0

    def doTask(self,taskobj):
        if taskobj.isCompleted == True:
            self.tasksDone += 1
        else:
            return "Nothing to do here."

    def vote(self, other):
        for c in other.crewmates:
            if c.name[0] == self.name[0]:
                if c.name != self.name and c.isAlive == True:
                    return c

        for i in other.impostors:
            if i.name[0] == self.name[0]:
                if i.name != self.name and i.isAlive == True:
                    return i

    def callMeeting(self, amgusObj):
        voteCount = {}
        maxVC = 0
        character = ""
        for cr in amgusObj.crewmates:
            votes = cr.vote(amgusObj)
            if votes.name in voteCount.keys():
                voteCount[votes.name] += 1
            else:
                voteCount[votes.name] = 1       
        for im in amgusObj.impostors:
            votes = im.vote(amgusObj)
            if votes.name in voteCount.keys():
                voteCount[votes.name] += 1
            else:
                voteCount[votes.name] = 1
        for name, count in voteCount.items():
            if count > maxVC:
                maxVC = count
                character = name
        for c in amgusObj.crewmates:
            if c.name == character:
                c.isAlive = False
                if type(c) == Impostor:
                    return "{} was An Impostor.".format(c.name)
                elif type(c) == Crewmate:
                    return "{} was not An Imposter.".format(c.name)
        for c in amgusObj.impostors:
            if c.name == character:
                c.isAlive = False
                if type(c) == Impostor:
                    return "{} was An Impostor.".format(c.name)
                elif type(c) == Crewmate:
                    return "{} was not An Imposter.".format(c.name)
     
 
    def __repr__(self):
        return "Crewmate(name: {}, color: {})".format(self.name, self.color)

    def __eq__(self, other):
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class Impostor:
    def __init__(self, n, c, ac = ()):
        self.name = n
        self.color = c
        self.accessories = ac
        self.isAlive = True
        self.eliminateCount = 0

    def eliminate(self, other): 
        if type(other) == Impostor:
            return "They're on your team -_-"
        elif type(other) == Crewmate:
            self.eliminateCount += 1
            other.isAlive = False
            
    def vote(self, other): 
        for k in other.crewmates:
            if k.name[0] == self.name[0]:
                if k.name != self.name and k.isAlive == True:
                    return k
                
        for u in other.impostors:
            if u.name[0] == self.name[0]:
                if u.name != self.name and u.isAlive == True:
                    return u
        
    def __str__(self):
        return "My name is {} and I'm an impostor.".format(self.name)

    def __repr__(self):
        return "Impostor(name: {}, color: {})".format(self.name, self.color)

    def __eq__(self, other):
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class AmongUs:
    def __init__(self, maxP):
        self.maxPlayers = maxP
        self.rooms = {}
        self.crewmates = []
        self.impostors = []

    def registerPlayer(self, other):
        if len(self.crewmates) + len(self.impostors) == self.maxPlayers:
            return "Lobby is full."
        for i in self.crewmates:
            if i.name == other.name:
                return "Player with name: {} exists.".format(i.name)
        for p in self.impostors:
            if p.name == other.name:
                return "Player with name: {} exists.".format(p.name)
        if type(other) == Crewmate:
            self.crewmates.append(other)
        elif type(other) == Impostor:
            self.impostors.append(other)

    def registerTask(self, taskobj, roomobj):
        '''
        print(taskobj)
        print(taskobj.name)
        print(roomobj)
        print(roomobj.name)
        print(self.rooms)
        '''
        for task in self.rooms.values():
            for i in task:
                if taskobj.name == i.name:
                    return "This task has already been registered."

        if roomobj.name in self.rooms.keys():
            self.rooms[roomobj.name].append(taskobj)
        else:
            self.rooms[roomobj.name] = [taskobj]

    def gameOver(self):
        c1 = 0
        i1 = 0
        for c in self.crewmates:
            if c.isAlive == True:
                c1 += 1
        for i in self.impostors:
            if i.isAlive == True:
                i1 += 1
        if c1 == 0:
            return "Defeat! All crewmates have been eliminated."
        elif i1 == 0:
            return "Victory! All imposters have been eliminated."
        else:
            return "Game is not over yet!"
                
    def __repr__(self):
        return "AmongUs(maxPlayers: {})".format(self.maxPlayers)
