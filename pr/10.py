# global_var = 20 # Глобальная переменная
#
# def show_global():
# print(f"Глобальная переменная: {global_var}")
#
# show_global()
# print(global_var) # Глобальная переменная доступна в любом месте


global_var = 20 # Глобальная переменная

def show_global(var):
#print(f"Глобальная переменная: {var}")

show_global(global_var)
print(global_var) # Глобальная переменная доступна в любом месте