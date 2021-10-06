from django.db import models
from django.forms import ModelForm

# Create your models here.
class S_app(models.Model):
    todo_id = models.CharField(unique=True, max_length=5)
    title = models.CharField(max_length=50)
    main_text = models.CharField(max_length=300)
    update_date = models.DateTimeField('date published')
class S_appForm(ModelForm):
    class Meta:
        model =S_app
        fields = ['todo_id', 'title', 'main_text', 'update_date']
        exclude = ['todo_id','update_date']
