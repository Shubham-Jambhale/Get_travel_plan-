from collections import defaultdict

def get_adjancency(adjancency_list,priorities):
    for i,j in priorities:
        adjancency_list[i].append(j)
    return adjancency_list

def get_travel_plan(cities,priorities):

    no_dependency = []
    values_list = []
    output_list=[]
    adjacency_list = defaultdict(list)
    output=[]
    
    dicti = get_adjancency(adjacency_list,priorities)
    
    for i in dicti.keys():
        values_list.append(set(dicti[i]))
        output_list.append(i)
        
    for i in range(len(cities)):
        if cities[i] not in dicti.keys():
            no_dependency.append(cities[i])
            
            
    while len(no_dependency)>0:
        x=no_dependency.pop()
        output.append(x)
        
        for i in range(len(values_list)):
            s = values_list[i]
            if x in s:
                s.remove(x)
                if len(s)==0:
                    no_dependency.append(output_list[i])
    output.reverse()
    if len(output)==len(cities):
        return output
    else:
        return []
        

print("---Output Begins --- ")
print()
output = get_travel_plan(['London', 'Mumbai', 'Medellín', 'São Paulo', 'Prague', 'Pune', 'Dhule','Akola'], 
                      [('Dhule', 'London'),('Pune', 'London'), ('Mumbai','London'), ('São Paulo', 'Medellín'),
                       ('Prague', 'Medellín'),('London','São Paulo'),('Mumbai','Dhule'),('Pune','Dhule'),
                       ('Pune','Mumbai')])
print(output)
print()
output=get_travel_plan(['London', 'Berlin', 'Medellín', 'São Paulo', 'Prague', 'Ladakh', 'Nice'],[('London','Medellín'), ('Medellín', 'São Paulo'), ('Prague', 'Berlin')])
print(output)
print()

output = get_travel_plan(['London', 'Berlin'],[('London','Berlin'), ('Berlin', 'London')])
print(output)
print()

output = get_travel_plan( ['London', 'Berlin','Medellin', 'Sao Paulo', 'Ladakh', 'Nice'],[('London', 'Medellin'), ('Medellin', 'Sao Paulo'), ('Berlin', 'Ladakh'), ('Sao Paulo', 'London') ])
print(output)
print()