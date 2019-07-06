from django.shortcuts import render, get_object_or_404
from .forms import ReportCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report
from django.shortcuts import redirect

# Create your views here.
@login_required
def  report_create(request):
	if request.method == 'POST':
		form = ReportCreateForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new = form.save(commit=False)
			new.user = request.user
			new.save()
			return redirect(new.get_absolute_url())
			messages.success(request, 'Report uploaded successfully')
		else:
			messages.success(request, 'Error uploading report')
	else:
		form = ReportCreateForm()
	return render(request, 'reports/create.html', {'form': form})

def report_detail(request, id, slug):
	report = get_object_or_404(Report, id=id, slug=slug)
	return render(request, 'reports/detail.html', {'report':report})