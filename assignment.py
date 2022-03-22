import sys
#This tests the algorithm component of the assignment,
#using the example in the text.

#Test dataset
data = [0,61,1,1,0,62,3,2,3,3]

#Define funciton that produces pairs
def pairwise(iterable):
    a = iter(iterable)
    return zip(a,a)

#Test of funciton
print('Simulated pairs:')
for p,q in pairwise(data):
    print(p,q)

#initialize array
emptyByteString = []

#Implementation of decoding algorithm
#First, take the first pair and assign to p,q
for p,q in pairwise(data):
    #If p == 0, append the value q to the array
    if p == 0:
        emptyByteString.append(q)
    #if p!=0, take q elements starting from index starting p indices from the end of the array.
    else:
        #Nasty looking, there is probably a better way to do this:
        emptyByteString.extend(emptyByteString[slice(len(emptyByteString)-p,len(emptyByteString)-p+q,1)])
    print('step',emptyByteString)

print('final:', emptyByteString)

#sys.stdout.buffer.write(bytes(emptyByteString))
