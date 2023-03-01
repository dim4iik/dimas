# try:
#     # name = "Dima"
#     print('start code')
#     # print(name)
#     print('No errors')
# except:
#     print('We have a problem (error)')
#
# print('This code after capsule.')




# try:
#     print('start code.')
#     print(name)
#     print(2 / 0)
#     print('no errors.')
# except (NameError, ZeroDivisionError):
#     print('We have an Error')
#
#
# print('code after capsule.')

# try:
#     try:
#         print('start  code')
#         print(error)
#         print('no errors')
#     except NameError as error:
#         print('error')
try:
        error = 'q'
        print('start  code')
        print(error)
        print('no errors.')
except NameError as error:
        print(error)
else:
    print('I am ELSE.')
finally:
    print('Finally code')
