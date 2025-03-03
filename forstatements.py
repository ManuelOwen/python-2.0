users = {'harold': 'active', 'denis': 'inactive', 'joe': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        # create a new dictionary with the same keys and values
        active_users = {}
        for user, status in users.items():
            if status =='active':
               active_users[user]=status
        print(active_users)
        