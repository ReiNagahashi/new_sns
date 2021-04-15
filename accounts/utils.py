from accounts.sz import GetFullUserSerializer

# ユーザーがログイン時にtokenのみならずユーザーの情報も同時に取得できるように設定する
def custom_jwt_response_handler(token,user=None,request=None):
    return {
        'token':token,
        'user':GetFullUserSerializer(user,context={'request':request}).data
    }