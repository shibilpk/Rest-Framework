def user(request):
	response = get_user_token(request, phone, decrypt_message(profile.password))

	if response.status_code == 200:
        response_data = {
            "StatusCode": 6000,
            "data":  {
                "data": response.json(),
                "title": "Verification Successful",
                "message": "Otp verified successfully",
                "is_active_user": is_active_user,
            }
        }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "data": response.json(),
                "title": "User not found",
                "message": "User not found Please contact us."
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)
