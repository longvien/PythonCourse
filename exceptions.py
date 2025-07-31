# catch an Exception    

acronyms = {'IDK': "I don't know",
            'LOL': 'Laugh out loud',}
try:
    definition = acronyms['TBH']
    print(definition)
except:
    print("The key doesn't exist")
finally:
    print('The defined acronyms are:')
    print('-----------------------------')
    for name, define in acronyms.items():
        for i in range(1):
            print(name, ':', define)
print('---------------------')
print('Program continues')





# raise an exception

# def remainder_calculating(a, b):
#     if a or b == 0:
#         raise ZeroDivisionError("Can't be divide by zero!")
#     result = a//b
#     remainder = a%b
#     print('The result of ' + str(a) + ' : ' + str(b) + ' is ' + str(result) + ' remain ' + str(remainder))
    
# remainder_calculating(10, 0)
