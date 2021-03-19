from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.utils import timezone

from hammingtests.models import HTestResults
from hammingtests.calc_hd import HDist

def index(request):
    return render(request, 'hammingtests_index.html')
def detail(request):
    latest_test_list = HTestResults.objects.order_by('-log_htest')[:5]
    context = {'latest_test_list': latest_test_list}
    return render(request, 'hammingtests_detail.html', context)

def inform(request):
    return render(request, 'hammingtests_inform.html')


def results(request):
    a = request.POST.get("string_A", "")
    b = request.POST.get("string_B", "")
    hd = HDist.hamming_distance(a,b)
    timestamp = timezone.now()
    if hd != False:
        new_record = HTestResults(string_A=a, string_B=b, hdistance=hd, log_htest=timestamp)
        new_record.save()
        return render(request, 'hammingtests_results.html', {'str_a':a,'str_b':b, 'hdist':hd,'ts':timestamp })
    else:
        return render(request, 'hammingtests_inform.html')

