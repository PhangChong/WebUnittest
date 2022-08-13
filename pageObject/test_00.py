def login(user, psw):
    if user != 'test':
        result = 'The user does not exist.'

    if user == 'test':
        if psw == '123456':
            result = 'success！'
        else:
            result = 'error！'
    return result
