from functools import wraps

from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


def superuser_required(func):
    @wraps(func)
    def _wrapped_view(request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user, is_active=True, is_superuser=True)
        if not user:
            raise Http404()
        return func(request, *args, **kwargs)

    return _wrapped_view


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = User.objects.filter(Q(username=request.user, is_active=True) &
                                   (Q(role=User.Role.ADMIN) | Q(role=User.Role.SUPERADMIN))).first()

        if not user:
            messages.error(request, _('Anda tidak memiliki otoritas pada halaman ini'),
                           button='OK', icon='error')
            return redirect('backoffice:index')
        return view_func(request, *args, **kwargs)

    return _wrapped_view
