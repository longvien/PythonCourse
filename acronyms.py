look_up = input('Which software acronym do you want to look up?\n')
found = False
with open('input.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break
    if not found: 
        print('Acronym not found!')

#Dòng found = False được dùng để đánh dấu rằng chưa tìm thấy dòng chứa từ khóa look_up. 
# Nếu sau khi duyệt xong toàn bộ file mà không tìm thấy dòng phù hợp, 
# biến found vẫn là False, từ đó bạn có thể in "Acronym not found!".




