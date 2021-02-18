from .models import mode

def current_user_posts_processor(request):
    user = request.user
    current_user_posts = mode.objects.filter(editor__username=user).order_by('-created_on')
    return {'current_user_posts':current_user_posts}
