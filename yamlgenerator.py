import random
import os
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def perfassessmentforagentnum(agentnum, gridsize):
    #fopen = open("statInput.yaml", "w")
    fopen.write('''agents:''')
    for num in range(agentnum):
        fopen.write('''
-   start: [''' + str(random.randint(1, gridsize-1)) + ',' + str(random.randint(1, gridsize-1)) + ''']    
    goal: [''' + str(random.randint(1, gridsize-1)) + ',' + str(random.randint(1, gridsize-1)) + ''']
    name: agent''' + str(num))


    ###first filer part

    fopen.write('''

map:
    dimensions: [''' + str(gridsize1) + ',' + str(gridsize1) + ''']
    obstacles:
        - !!python/tuple [''' + str(random.randint(1, gridsize)) + ', ' + str(random.randint(1, gridsize)) + ''']
        - !!python/tuple [''' + str(random.randint(1, gridsize)) + ', ' + str(random.randint(1, gridsize)) + ''']
        - !!python/tuple [''' + str(random.randint(1, gridsize)) + ', ' + str(random.randint(1, gridsize)) + ''']       
        - !!python/tuple [''' + str(random.randint(1, gridsize)) + ', ' + str(random.randint(1, gridsize)) + ''']
        # - !!python/tuple [2, 1]

    pickupStation:
    ''' + pickupstation1 + '''
    ''' + pickupstation1 + '''
    ''' + pickupstation1 + '''
    deliveryStation:
         - !!python/tuple [0, 0]

    ''')

    ##END OF FIRST FILLER PART

    ##SECOND FILLER PART

    fopen.write('''
order:
    orders_:''')
    for z in range(1, ordercount-1):
        fopen.write('''
            -   id_code: o''' + str(z) + '''
                timestep: ''' + str(z) + '''
                requested_quantities: [1]
                pickupStation:
                 ''' + pickupstation1 + '''

            -   id_code: i''' + str(z) + '''
                timestep: ''' + str(z) + '''
                requested_quantities: [1]
                pickupStation:
                 ''' + pickupstation2 + '''

            -   id_code: z''' + str(z) + '''
                timestep: ''' + str(z) + '''
                requested_quantities: [1]
                pickupStation:
                 ''' + pickupstation3 + '''

    ''')

    ##END OF SECOND FILLER PART




    fopen.write('''
dynamic_obstacles: {}
    ''')
    fopen.close()





gridsize1 = 20
#agentsnumber = 20
ordercount = 50
pickupstation1 = '''   - !!python/tuple [''' + str(random.randint(1, gridsize1)) +', '+ str(random.randint(1, gridsize1)) + ''']'''
pickupstation2 = '''   - !!python/tuple [''' + str(random.randint(1, gridsize1)) +', '+ str(random.randint(1, gridsize1)) + ''']'''
pickupstation3 = '''   - !!python/tuple [''' + str(random.randint(1, gridsize1)) +', '+ str(random.randint(1, gridsize1)) + ''']'''
averages = []

for xx in range (2, 5):
    fopen = open("statInput.yaml", "w")
    perfassessmentforagentnum(xx, gridsize1)
    os.system('python environment.py')
    ropen = open('averagedeliverytimenow.txt', 'r')
    averages.append(ropen.readline())
    ropen.close()
print(averages)

