from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from safe_manage.models import Examination,Problem,Rectification,ImgProblem
from .forms import ExaminationForm,ProblemForm,RectificationForm,ProblemPassForm,CommentForm,ImgProblemForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	"""主页"""
	return render(request, 'safe_manage/index.html')
	
def examinations(request):
	"""显示所有的检查"""
	examinations = Examination.objects.order_by('-date_added')
	problems = set()
	for e in examinations:
		for p in e.problem_set.all():
			problems.add(p)
	context = {'examinations':examinations,'problems':problems}
	return render(request, 'safe_manage/examinations.html', context)

def problems(request,examination_id):
	"""显示某次检查发现的所有问题"""
	e = Examination.objects.get(id=examination_id)
	p = e.problem_set.all()
	problems = p
	i = set()
	for pp in problems:
		for imgs in pp.imgproblem_set.all():
			i.add(imgs)
	context = {'examination':e,'problems':p,'imgproblem':i}
	return render(request, 'safe_manage/problems.html', context)
	
def rectification(request,problem_id):
	"""显示问题的整改措施"""
	p = Problem.objects.get(id=problem_id)
	i = p.imgproblem_set.all()
	r = p.rectification_set.all().order_by('-date_added')
	context = {'problem':p,'rectification':r,'imgproblem':i} 
	return render(request, 'safe_manage/rectification.html', context)

@login_required	
def new_examination(request):
	"""添加新检查"""
	if request.method!='POST':
		form = ExaminationForm()
		context = {'form':form}
		return render(request,'safe_manage/new_examination.html',context)
	else:
		form = ExaminationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('safe_manage:examinations'))	

@login_required			
def new_problem(request,examination_id):
	"""在检查中发现的问题"""
	examination = Examination.objects.get(id=examination_id)
	if request.method!='POST':		
		form = ProblemForm()
	else:
		form = ProblemForm(request.POST)
		if form.is_valid():
			new_problem = form.save(commit=False)
			new_problem.Examination = examination
			new_problem.save()
			return HttpResponseRedirect(reverse('safe_manage:problems',args=[examination_id]))
	context = {'examination':examination,'form':form}
	return render(request,'safe_manage/new_problem.html',context)

@login_required	
def edit_examination(request,examination_id):
	"""编辑检查的内容"""
	examination = Examination.objects.get(id=examination_id)
	if request.method != 'POST':
		form = ExaminationForm(instance=examination)
		context = {'examination':examination,'form': form}
		return render(request, 'safe_manage/edit_examination.html', context)
	else:
		form = ExaminationForm(instance=examination, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('safe_manage:examinations'))

@login_required		
def edit_problem(request,problem_id):
	"""编辑检查的内容"""
	problem = Problem.objects.get(id=problem_id)	
	examination = problem.Examination
	if request.method != 'POST':
		form = ProblemForm(instance=problem)
		context = {'examination':examination,'problem':problem,'form': form}
		return render(request, 'safe_manage/edit_problem.html', context)
	else:
		form = ProblemForm(instance=problem, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('safe_manage:problems',args=[examination.id]))

@login_required			
def new_rectification(request,problem_id):
	"""新增整改措施"""
	problem = Problem.objects.get(id=problem_id)
	if request.method!='POST':
		form = RectificationForm()
		context = {'problem':problem,'form':form}
		return render(request,'safe_manage/new_rectification.html',context)
	else:
		form = RectificationForm(request.POST)	
		if form.is_valid():
			new_rectification = form.save(commit=False)
			new_rectification.Problem = problem
			new_rectification.save()
			return HttpResponseRedirect(reverse('safe_manage:rectification',args=[problem_id]))

@login_required			
def edit_rectification(request,rectification_id):
	"""编辑整改措施的内容"""
	rectification = Rectification.objects.get(id=rectification_id)
	problem = rectification.Problem
	if request.method != 'POST':
		form = RectificationForm(instance=rectification)
		context = {'problem':problem,'form': form}
		return render(request, 'safe_manage/edit_rectification.html', context)
	else:
		form = RectificationForm(instance=rectification, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('safe_manage:rectification',args=[problem.id]))

@login_required
def new_comment_pass(request,problem_id):
	"""对问题的整改进行合格确认"""
	problem = Problem.objects.get(id=problem_id)
	if request.method!='POST':
		form = ProblemPassForm()
		context = {'problem':problem,'form':form}
		return render(request,'safe_manage/new_comment_pass.html',context)
	else:
		form = ProblemPassForm(instance=problem, data=request.POST)	
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('safe_manage:rectification',args=[problem_id]))

@login_required			
def new_comment(request,rectification_id):
	rectification = Rectification.objects.get(id=rectification_id)
	problem = rectification.Problem
	if request.method!='POST':
		form = CommentForm()
		context = {'rectification':rectification,'form':form}
		return render(request,'safe_manage/new_comment.html',context)
	else:
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.Rectification = rectification
			new_comment.save()
			return HttpResponseRedirect(reverse('safe_manage:rectification',args=[problem.id]))		
		
@login_required				
def upload(request,problem_id):
	"""上传问题的图片"""
	problem = Problem.objects.get(id=problem_id)
	examination = problem.Examination
	examination_id = examination.id
	if request.method != 'POST':
		#form = ImgProblemForm()
		#context = {'form':form,'problem':problem}
		return render(request,'safe_manage/upload.html')
	else:
		form = ImgProblemForm(request.POST,request.FILES)
		new_img = form.save(commit=False)
		new_img.Problem = problem
		new_img.save()
		
		return HttpResponseRedirect(reverse('safe_manage:problems',args=[examination_id]))
		
def deleteimg(request,img_id):
	imgproblem = ImgProblem.objects.get(id = img_id)
	examination_id = imgproblem.Problem.Examination.id
	imgproblem.delete()
	return 	HttpResponseRedirect(reverse('safe_manage:problems',args=[examination_id]))	
	
