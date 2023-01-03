import sys
def sample_function(*tenants: str) -> str:
    """Testing the function
    :param tenants: pass in tenant names as short names
    :returns: a tuple of tenant names
    """
    this_function_name = sys._getframe(  ).f_code.co_name
    print('this_function_name: ', this_function_name)
    print(tenants)
    for i, tenant in enumerate(tenants,1):
        print(i, tenant, sep=': ')
    print("DONE!")

if '__main__'== __name__:
    sample_function("hm", "molina", "m1", "hello")

