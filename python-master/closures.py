
def outer_fn():

    def inner_fn():
        print("Hello from inner fn")

    inner_fn()



fn_ref = outer_fn

###closure refrence outlive the original outer function , we can still call the fn through refrence 
del outer_fn

#### here we have deleted the outer_fn() but still able to call the fn through refrence
fn_ref()