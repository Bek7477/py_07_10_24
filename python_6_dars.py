# while True:
#     try:
#         num1 = int(input('num1 = '))
#         num2 = int(input('num2 = '))
#         belgi = input('belgi = ')
        
#         if belgi == '+':
#             res = num1 + num2
#         if belgi == '/':
#             res = num1 / num2
#         if belgi == '-':
#             res = num1 - num2
#         if belgi == '*':
#             res = num1 * num2        
#     except ZeroDivisionError:
#         print("HQS0BB")
#     except ValueError:
#         print("faqat butun son kriting:")
#     else:
#         print(res)
#         break

# sum = 0
# while True:
    
#     try:
        
#         n = input("n = ")

#         if n == 'c':
#             print(sum)
#             break
#         elif n.isdigit:
#             sum += int(n)  
#         else:
#             raise ValueError("Oops")    
#     except ValueError:
#         print("Valude Error")

# def int_num(value):
#     try:
#         result = int(value)
#         return result
#     except ValueError:
#         return "Buning iloji yo'q"

# n = input("n = ")
# print(int_num(n))  

# class LengthMismatchError(Exception):
#     pass

# class CaseMismatchError(Exception):
#     pass

# class FullMismatchError(Exception):
#     pass

# def parolni_tekshirish():
#     try:
#         parol1 = input("Parolni kiriting: ")
#         parol2 = input("Qayta parolni kiriting: ")

#         if len(parol1) != len(parol2):
#             raise LengthMismatchError("Parollar bir xil uzunlikda bo'lishi kerak.")

#         if parol1.lower() != parol2.lower():
#             raise CaseMismatchError("Parollar katta kichiklikda farq qilmaydi.")

#         if parol1 != parol2:
#             raise FullMismatchError("Parollar bir xil emas.")

#         print("Parollar muvaffaqiyatli tekshirildi!")

#     except LengthMismatchError as e:
#         print(f"Uzunlik xatosi: {e}")

#     except CaseMismatchError as e:
#         print(f"Katta kichiklik xatosi: {e}")

#     except FullMismatchError as e:
#         print(f"Ikki parol farqli: {e}")

# parolni_tekshirish()



def o_sish_tardibida(lst):
    if not lst:
        return 0
    
    count = 0
    length = len(lst)
    
    i = 0
    while i < length:
        current_length = 1
        j = i + 1
        
        while j < length and lst[j] > lst[j - 1]:
            current_length += 1
            j += 1
        
        if current_length > 1:
            count += 1
        
        i = j 
        
    return count
def Full_list(n,lst: list):
    for i in range(n):
        qiymat = int(input(">>> "))
        lst.append(qiymat)
        
    return lst

lst = []
n = int(input("list uzunligini kiritng: "))
print(Full_list(n,lst))

result = o_sish_tardibida(lst)
print("O'sish tartibida kelgan to'plamlar soni:", result)
