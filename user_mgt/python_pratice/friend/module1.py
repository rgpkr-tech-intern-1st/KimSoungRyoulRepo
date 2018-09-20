def send_message(name, message):
    print('success to send message!!!')
    print(name, message)


if __name__ == '__main__':
    while True:
        input_num = input('input command: ')

        if input_num == '3':
            name = input('friend name : ')
            message = input('message : ')
            send_message(name, message)
