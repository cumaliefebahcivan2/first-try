brother_list = []
sister_list = []
sibling_list = []
parent = ""
children = []
def gender(pname):
    if pname[0] == pname[0].lower():
        return "male"
    elif pname[0] == pname[0].upper():
        return "female"

def parentfinder(T,pname):
    global parent
    if pname in T:
        parent = T[0]
    else:
        for i in range(0,len(T)):
            if type(T[i]) == list:
                if T[i][0] == pname:
                    parent = T[0]
                    break
                parentfinder(T[i],pname)
    if parent == pname:
        return ""
    else:
        return parent
def childrenfinder(T,pname):
    global children
    if (pname in T) and T[0] == pname:
        for i in range(1,len(T)):
            if type(T[i]) == list:
                children.append(T[i][0])
            else:
                children.append(T[i])
    else:
        for j in range(1,len(T)):
            if type(T[j]) == list:
                childrenfinder(T[j],pname)
    return children


def process(T):
    global brother_list
    global sister_list
    global sibling_list
    brother = []
    sister = []
    sibling = []
    for i in range(1,len(T)):
        if type(T[i]) == list:
            if gender(T[i][0]) == "male":
                parameter = T[i][0]
                brother.append(parameter)
            else:
                parameter = T[i][0]
                sister.append(parameter)
            sibling.append(T[i][0])
            process(T[i])
        else:
            if gender(T[i]) == "male":
                brother.append(T[i])
            else:
                sister.append(T[i])
            sibling.append(T[i])
    sibling_list.append(sibling)
    sister_list.append(sister)
    brother_list.append(brother)

def siblings(T,pname):
    process(T)
    answer1 = []
    global sibling_list
    if pname in sibling_list:
        answer1 = sibling_list[i]
    else:
        for i in range(0,len(sibling_list)):
            if type(sibling_list[i]) == list:
                if pname in sibling_list[i]:
                    answer1 = sibling_list[i]
                    break
    if pname in answer1:
        answer1.remove(pname)
    return answer1

def brothers(T,pname):
    answer1 = []
    deleteobj = []
    answer1 = siblings(T,pname)
    for i in range(0,len(answer1)):
        if gender(answer1[i]) == "female":
            deleteobj.append(answer1[i])
    for j in deleteobj:
        answer1.remove(j)
    if pname in answer1:
        answer1.remove(pname)
    return answer1

def sisters(T,pname):
    answer1 = []
    deleteobj = []
    answer1 = siblings(T, pname)
    for i in range(0, len(answer1)):
        if gender(answer1[i]) == "male":
            deleteobj.append(answer1[i])
    for j in deleteobj:
        answer1.remove(j)
    if pname in answer1:
        answer1.remove(pname)
    return answer1

def uncles(T,pname):
    process(T)
    parent1 = parentfinder(T,pname)
    return brothers(T,parent1)

def aunts(T,pname):
    process(T)
    parent1 = parentfinder(T,pname)
    return sisters(T,parent1)

def cousins(T,pname):
    global children
    answer1 = []
    process(T)
    parent1 = parentfinder(T, pname)
    parentsofcousins = siblings(T,parent1)
    for a in range(0,len(parentsofcousins)):
        children = []
        answer1 += childrenfinder(T,parentsofcousins[a])
    return answer1
