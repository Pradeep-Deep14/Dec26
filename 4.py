def addition(**kwargs):
    total=0
    for key,value in kwargs.items():
        total+=value
    return total

print(addition(x=1,y=2,z=3,w=4))