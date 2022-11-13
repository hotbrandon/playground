# a closure is a function that closes over(or encloses) the set of its free variables
# https://www.youtube.com/watch?v=swU3c34d2NQ
# a closure is an inner function that rememebers and has access to variables in the
# local scope in which it was created even after the outer function has finished executing

def create_closure(func):
    def logger_func(*args):
        print('calling function {} with arguments {}'.format(func.__name__, args))

    return logger_func


def create_account(name):
    print('account {name} created'.format(name))


def deposit(account_name, amount):
    print('account {name} deposits {}'.format(account_name, amount))


account_logger = create_closure(create_account)
deposit_logger = create_closure(deposit)

account_logger('brandon')
deposit_logger('brandon', 2000)
