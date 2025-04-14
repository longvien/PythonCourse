#self: Là tham số đầu tiên của mọi phương thức trong lớp. 
#Nó đại diện cho đối tượng cụ thể mà bạn đang tạo ra. Chẳng hạn, khi bạn tạo một con chó, 
#self chính là con chó đó.

#self.name = name: Dòng này có nghĩa là bạn gán giá trị của name (tên bạn đưa vào khi tạo đối tượng) cho 
#thuộc tính name của đối tượng (ví dụ là con chó). Ví dụ, nếu bạn muốn tạo một con chó tên là "Buddy", 
#bạn sẽ truyền "Buddy" vào như một đối số. Lúc này, giá trị "Buddy" sẽ được gán cho thuộc tính name của con 
#chó.

#self.breed = breed: Tương tự, bạn gán giá trị của breed 
#(giống loài bạn đưa vào khi tạo đối tượng) cho thuộc tính breed của đối tượng. Ví dụ, giống loài 
#có thể là "Golden Retriever".

#Vậy khi bạn tạo một đối tượng, như một con chó, bằng cách 
#gọi dog = Animal("Buddy", "Golden Retriever"), thì:

#dog.name sẽ lưu trữ giá trị "Buddy" 
#(tên của con chó).
#dog.breed sẽ lưu trữ giá trị "Golden Retriever" 
#(giống loài của con chó).
#Cả hai giá trị này được lưu trong đối tượng dog 
#để bạn có thể sử dụng sau này.