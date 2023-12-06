from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)
    context = {
        'contacts': contacts,
    }
    return render(  request, 'contact/index.html',   context)


def contact(request, contact_id):
    #single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    '''
    if single_contact is None:
        raise Http404('contato não encontrado')

    '''    
    context = {
        'contact': single_contact,
    }
    return render(  request, 'contact/contact.html',   context)


def search(request):


    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)

    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def create(request):
    return render(request, 'contact/create.html')


