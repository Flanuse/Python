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




    # def process_request(self, request):
    #     paths = ['/adminback/login_back/', '/adminback/register_back/', '/user/login/']
    #     if request.path in paths:
    #         return None
    #     ticket = request.COOKIES.get('ticket')
    #     if not ticket:
    #         return HttpResponseRedirect(reverse('adminback:login_back'))
    #     user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
    #
    #     if user_ticket:
    #         if datetime.now() > user_ticket.out_time.replace(tzinfo=None):
    #             user_ticket.delete()
    #             return HttpResponseRedirect(reverse('adminback:login_back'))
    #         else:
    #             request.user = user_ticket.user
    #             UserTicketModel.objects.filter(Q(user=user_ticket.user) & ~Q(ticket=ticket)).delete()
    #             return None
    #     else:
    #         return HttpResponseRedirect(reverse('adminback:login_back'))


# class Middleware(MiddlewareMixin):
