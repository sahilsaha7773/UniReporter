from django.shortcuts import render, get_object_or_404
from .forms import ReportCreateForm, CommentForm
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