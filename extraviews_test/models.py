from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Child1(models.Model):
    name = models.CharField(max_length=255)
    child1_column = models.CharField(max_length=255)
    Parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Child2(models.Model):
    name = models.CharField(max_length=255)
    child2_column = models.CharField(max_length=255)
    comments2 = models.CharField(max_length=255,null=True)
    Parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Child3(models.Model):
    name = models.CharField(max_length=255)
    child3_column = models.CharField(max_length=255)
    comments3 = models.CharField(max_length=255,null=True)
    Parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name