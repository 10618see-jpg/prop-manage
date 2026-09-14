from django.contrib.auth.decorators import user_passes_test


# ゆーざーのroleを確認するデコレーター
def role_required(allowed_roles):
    def test_func(user):
        return user.role in allowed_roles

    return user_passes_test(test_func)
