from django.shortcuts import render, get_object_or_404
from .forms import ReportCreateForm, CommentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report, Comment
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

@login_required
def report_delete(request, id, slug):
    report= get_object_or_404(Report, id=id, slug=slug)    
    if request.method=='POST':
        report.delete()
        return HttpResponse('deleted')
    return render(request, 'reports/del_conf.html', {'object':report})

@login_required
def delete_done():
	return render(request, 'reports/del_done.html')

def report_detail(request, id, slug):
	report = get_object_or_404(Report, id=id, slug=slug)

	comments = report.comments.filter(active=True)
	new_comment = None
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.report = report
			new_comment.save()
	else:
		comment_form = CommentForm()

	return render(request, 'reports/detail.html', {'report':report, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form})