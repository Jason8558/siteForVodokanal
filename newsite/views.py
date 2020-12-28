from django.shortcuts import redirect


def redirect_homepage(request):
    return redirect('posts_list_url', permanent=True)
