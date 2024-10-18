immutable_var = 1,2,3, 'Павлик', True, 0.25                 # Создаём кортеж

immutable_var1 = tuple([4,5,6, "Василий", False, 2.52])     # Или используя функцию tuple ([список])

print(immutable_var)
print(immutable_var1)

print(immutable_var1 + immutable_var * 2)                   # tuple - кортежи можно склеивать и умножать

# immutable_var[0]=300                                      # Значения элементов кортежа нельзя изменить,
# потому что кортежи — это неизменяемый тип данных и были разработаны специально для этого.


mutable_list = [1,2,3, 'Павлик', True, 0.25]                # Создаем список используя []

mutable_list[3]='Николай', False, 15                        # Делаем изменения, внутрь списка можно вставить кортеж

print(mutable_list)