import mini

while True:
    command = input('>> ')

    if command in [':x', '::exit']:
        break
    
    result, error = mini.run(command)

    if error:
        print(error.as_string())
    else:
        print(result)