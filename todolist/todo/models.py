from django.db import models

# Create your models here.

class TodoList(models.Model):
    todo_title = models.CharField(max_length=100, null=False)
    todo_content = models.TextField(null=True)
    deadline = models.DateTimeField()
    priority = models.IntegerField(default=3) # 0-5; the smaller, the more urgent
    done = models.BooleanField(default=False) # if it's true, it means it's done

    def __str__(self):
        return self.todo_title

