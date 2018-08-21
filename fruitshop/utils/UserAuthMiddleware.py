from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from adminback.models import UserTicketModel
from users.models import TicketModel


class UserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        paths = ['/user/login/', '/user/register/']
        if request.path in paths:
            return None
        session_id = request.COOKIES.get('session_id')
        if not session_id:
            return HttpResponseRedirect(reverse('user:login'))
        user_session_id = TicketModel.objects.filter(session_id=session_id).first()
        if user_session_id:
            if datetime.now() > user_session_id.out_time.replace(tzinfo=None):
                user_session_id.delete()
                return HttpResponseRedirect(reverse('user:login'))
            else:
                request.user = user_session_id.user
                TicketModel.objects.filter(Q(user=user_session_id.user) & ~Q(session_id=session_id)).delete()
                return None
        else:
            return HttpResponseRedirect(reverse('user:login'))

