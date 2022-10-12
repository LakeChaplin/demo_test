# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# def get_formated_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formated_name('jimi', 'hendrix')
# print(musician)

# musician2 = get_formated_name('john','hooker','lee' )
# print(musician2)




# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)
# print(type(musician))

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print('\nPlease tell your name: ')
#     print("(enter 'q' at any time to quit)")
#     f_name = input('First name: ')
#     if f_name == 'q':
#         break
#     l_name = input('Last name: ')
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")

# def city_country(city_name, country_name):
#     full_name = f"{city_name} in {country_name}"
#     return full_name

# print(city_country('Moscow', 'Russia'))
# print(city_country('Delhi', 'India'))



# def make_album(musician_name, album_name, track_count=None):
#     final_dict = {'Album': album_name,
#                   'Muscian_name': musician_name}
#     if track_count:
#         final_dict['track_count'] = track_count

#     return final_dict

# while True:
#     print(f"You can add new pair musicion/album (for finish enter 'q')")
#     musicion_input = input(f"\nPlease enter name of musician: ")
#     if musicion_input == 'q':
#         break 
#     album_input = input(f"\nPlease enter name of album: ")
#     if album_input == 'q':
#         break

#     formatted_info = make_album(album_name=album_input, musician_name=musicion_input)
#     print(formatted_info)



# print(make_album('Nirvana', 'Nevermind', 7))
# print(make_album('Linkin Park', 'Meteora'))
# print(make_album('AC/DC', 'Back in black', 11))

# def greet_users(names):
#     for name in names:
#         print(f"Hello dear {name.title()}")

# usernames = ['andrey', 'dima', 'nikolay']
# greet_users(usernames)

# unprinted_designs = ['phone case', 'robot pendant','dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f'Printing model: {current_design}')
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for comleted_model in completed_models:
#     print(comleted_model)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f'Printing model: {current_design}')
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for comleted_model in completed_models:
#         print(comleted_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)




# messages = ['message-1','message-2', 'message-3','message-4']
# sent_messages = []

# def send_messages(messages, sent_messages):
#     for message in messages:
#         print(message)
#         sent_messages.append(message)


# send_messages(messages, sent_messages)

# print(messages)
# print(sent_messages)


