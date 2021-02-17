
"""
    creating list using list comprehension
"""

create_list = [i for i in range(10, 50)]
print(create_list)

"""
     using if condition in list comprehension
"""

even_number = [i for i in range(11, 41) if i % 4== 0]
print(even_number)
"""
     using if & else condition in list comprehension
"""

even = [i if i % 6== 0 else "odd" for i in range(10, 20)]
print(even)

"""
    create a dictionary using dictionary comprehension
"""

create_dict = {i: "number" for i in range(10, 20)}
print(create_dict)

"""
    using if condition in dictionary comprehension
"""

even = {i: "even" for i in range(10, 100) if i % 2 == 0}
print(even)

"""
    using if & else condition in list comprehension
"""

even_odd = {i: "even" if i  % 4== 0 else "odd" for i in range(10, 20)}
print(even_odd)
