# #1
# def good() :
#     return ['Harry', 'Ron', 'Hermione']
#
# #2
# def get_odds(start=0, end=9, step=1) :
#     number = start
#     while number <= end :
#         if number % 2 == 1 :
#             yield number
#         number += step
#
# s = 0
# for i in get_odds() :
#     s += 1
#     if s == 3 :
#         print(i)

#3
# def test(func) :
#     def start_end(*args, **kwargs) :
#         print('start')
#         result = func(*args, **kwargs)
#         print(result)
#         print("end")
#         return result
#     return start_end
#
# @test
# def add(n1, n2) :
#     return n1 + n2
#
# add(1,3)


#4
class OopsException(Exception) :
    pass
try :
    raise OopsException
except :
    print("Caught an oops")
