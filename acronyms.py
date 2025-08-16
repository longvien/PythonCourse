def find_acronym():
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


def add_acronym():
    acronym = input('Which acronym would u like to input?\n')
    definition = input("What's the definition of the acronym?\n")
    with open('input.txt', 'w') as file:
        file.write(acronym + ' - -' + definition + '\n')


def main():
    choice = input('Would you like to find(F) or add(A) an  acronym?\n')
    if choice == 'A':
        add_acronym()
    elif choice == 'F':
        find_acronym()
main()




