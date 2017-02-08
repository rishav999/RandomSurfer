import random
def transitionMatrix(linkCounts):
    '''
    Returns a transition matrix given a link-count matrix

    Inputs: LinkCounts
    This is the matrix that contains the count of total access to each page

    Output:
    A Matrix that has the probability of getting to each page
    '''
    newList=[]
    newBigList=[]
    BigList=linkCounts
    for item in BigList:
        newList=[]
        listSize=len(item)
        for NumLinks in item:            
            if sum(item)!=0:
                jprobability=(.90/sum(item))*NumLinks
            else:
                jprobability=0
            lprobability=0.02
            newList.append(jprobability+lprobability)
        newBigList.append(newList)
    return newBigList

def randomSurfer(transitionMatrix, M):
    '''
    Runs Random Surfer for M steps
    Returns a vector of page ranks

    Inputs:
    transitionMatrix, which is the probability of going to each page
    M, which is the total number of times you want the person to move
    '''
    countMatrixSmall=[0]*len(transitionMatrix)
    countMatrixSmall[0] = 1 #starting at the first page
    countMatrixBig=transitionMatrix
    index=0
    for i in range(M-1):
        curr_prob=0.0
        rand=random.random()
        for probabilities in range(len(countMatrixBig[index])):
            curr_prob+=countMatrixBig[index][probabilities]             
            if 0.0<=rand<=curr_prob: #checking where the random number lies on the list of cumulative probabiities
                index=probabilities
                countMatrixSmall[index]+=1
                break;             
    for i in range(len(countMatrixSmall)):
         countMatrixSmall[i]=countMatrixSmall[i]*1.0/float(M)
    return countMatrixSmall

def powerRanksHelper(transitionMatrix, prev):
    '''
    Computes the matrix multiplication and finds the new ranks of the pages
    transitionMatrix
    prev, which is the previous position of the vector that cotains the visit counts to a page
    '''
    initial=[0.0]*len(prev) #empty array of the same size as the old page ranks
    for row in range(len(transitionMatrix)):
        for column in range(len(transitionMatrix)):
            initial[row]+=prev[column]*transitionMatrix[column][row] #doing the matrix multiplication to find the next pagerank
    return initial

def powerRanks(transitionMatrix, M):
    '''
    Calculates PageRanks using the power method for M multiplications
    Returns a vector of PageRanks
    '''
    rank=[0.0]*len(transitionMatrix)
    rank[0]=1
    for i in range(M):
        rank=powerRanksHelper(transitionMatrix,rank) #creating the powerranks
    return rank

def loadWebGraph(filename):
    '''
    Returns a link-count matrix based on an input file describing a web graph.
    '''
    
    with open(filename, 'rt') as f:
        N = int(f.readline().strip('"'))
        LC = [ [0] * N for i in range(N) ]
        for line in f:
            tokens = list(map(int, line.split()))
            for i in range(1, len(tokens), 2):
                src = tokens[i-1]
                dst = tokens[i]
                LC[src][dst] += 1    
    return LC

def main():
    filename1='tiny.txt'
    filename2='bigger.txt'
    #linkCounts=loadWebGraph(filename2)
    linkCounts=[[0,1,0,0,0],[0,0,2,2,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,1,0,0]]
    m=transitionMatrix(linkCounts)
    for item in m:
        print item
    print('---')
    k=randomSurfer(m,3000)
    print k
    print('---')
    k2=powerRanks(m,1000)
    print k2


if __name__ == "__main__":
    main()

