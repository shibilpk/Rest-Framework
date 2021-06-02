def generate_serializer_errors(args):
	message = ''
	for key,values in args.iteritems():
		error_message = ""
		for value in values:
			error_message +=value + ","
		error_message = error_message[:-1]

		message += "%s : %s |" %(key,error_message)
	return message[:-3]


def generate_serializer_errors(args,many=False):
    message = {}
    if many:
        for args in args:
            for key, values in args.items():
                error_message = ""
                
                for index, value in enumerate(values):
                    error_message += value

                    if(index + 1 == len(values)):
                        break
                        error_message += ","

                if key == 'non_field_errors':
                    key = 'error'
                if key.capitalize() in message:
                    message[key.capitalize()] += error_message
                else:
                    message[key.capitalize()] = error_message
    else:
        for key, values in args.items():
            error_message = ""
            for index, value in enumerate(values):
                error_message += value

                if(index + 1 == len(values)):
                    break
                    error_message += ","

            if key == 'non_field_errors':
                key = 'error'
            message[key.capitalize()] = error_message
    return message


def get_user_token(request, user_name, password):
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"username": "' + user_name + '", "password":"' + password + '"}'

    protocol = "http://"
    if request.is_secure():
        protocol = "https://"

    web_host = request.get_host()
    request_url = protocol + web_host + "/api/v1/auth/token/"

    response = requests.post(request_url, headers=headers, data=data)

    return(response)