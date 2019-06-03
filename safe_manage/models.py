from django.db import models

# Create your models here.

class Examination(models.Model):
	"""一次检查的类"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True) #检查上传的时间
	datecheck = models.DateField() #执行检查的时间
	def __str__(self):
		"""返回字符串表示"""
		return self.text
		
class Problem(models.Model):
	"""检查到的问题，和Examination关系为一对多"""
	ifdone = models.BooleanField(default=False)  #是否已经整改，默认为否
	Examination = models.ForeignKey(Examination,on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True) #问题上传的时间
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text
	def set_bool(self):
		self.ifdone = True
		
class ImgProblem(models.Model):
	"""检查出问题的图片"""
	Problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
	img = models.ImageField(upload_to = 'media')			
		
class Rectification(models.Model):
	"""整改措施，和Problem关系为一对多"""
	Problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True) #整改措施上传的时间
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text
		
class Comment(models.Model):
	"""对整改措施进行评价"""
	Rectification = models.OneToOneField(Rectification,on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True) #评论上传的时间
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text[:50]
