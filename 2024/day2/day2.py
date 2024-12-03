with open('day2\\data\\input.txt', 'r') as f:
    data = f.readlines()


def check_safe(levels, nested=False):
    direction = None
    bad = 0

    for i in range(1, len(levels)):
        if(direction is None):
            if(levels[i] < levels[i-1]):
                direction = 1
            elif(levels[i] > levels[i-1]):
                direction = -1
        else:
            if(direction == 1 and levels[i] > levels[i-1]):
                list_a = levels.copy()
                list_a.pop(i)
                
                list_b = levels.copy()
                list_b.pop(i-1)
                if(nested == True or (nested == False and check_safe(list_a, nested=True) == 0 and check_safe(list_b, nested=True) == 0)):
                        bad = 1 
                        break;
                
            elif(direction == -1 and levels[i] < levels[i-1]):
                list_a = levels.copy()
                list_a.pop(i)
                
                list_b = levels.copy()
                list_b.pop(i-1)
                if(nested == True or (nested == False and check_safe(list_a, nested=True) == 0 and check_safe(list_b, nested=True) == 0)):
                        bad = 1 
                        break;
        
        if(abs(levels[i]-levels[i-1]) > 3 or abs(levels[i]-levels[i-1]) < 1):
            list_a = levels.copy()
            list_a.pop(i)
            
            list_b = levels.copy()
            list_b.pop(i-1)
            if(nested == True or (nested == False and (check_safe(list_a, nested=True) == 0 and check_safe(list_b, nested=True) == 0))):
                    bad = 1 
                    break;

    if bad == 1 and nested == False:
        for i in range(len(levels)):
            levels_a = levels.copy()
            levels_a.pop(i)

            if(check_safe(levels_a, nested=True) == 1):
                return 1
                
    return 1 if bad == 0 else 0

safe = 0
for report in data:
    levels = list(map(int, report.replace('\n', '').split(' ')))
    
    safe += check_safe(levels)
    
    

print(safe)

