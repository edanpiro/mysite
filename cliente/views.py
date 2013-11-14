# -*- coding: utf-8 -*-
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__email__ = 'pimentelrojas@gmail.com'
__url__ = ''
__date__ = "2013-11-08"
__updated__ = "2013-11-08"

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from cliente.models import Cliente


def index_cliente(request):
    '''Index Page'''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    datos = Cliente.objects.order_by('nombre').all()
    context = {'posts': datos}
    return render(request, 'index_cliente.html', context)