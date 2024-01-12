from django.contrib import admin
from . models import *
# Register your models here.
class Packages_display(admin.ModelAdmin):
    list_display=['image','description']
class Blog_display(admin.ModelAdmin):
    list_display=['image','description']

class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','subject']

class Enquiry_display(admin.ModelAdmin):
    list_display=['name','email','phone','message']

class Appointment_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','age','gender','address','date','time']

class Sub_package_display(admin.ModelAdmin):
    list_display=['name','test1','test2','test3','test4','test5','cost','image','package']

class Branch_display(admin.ModelAdmin):
    list_display=['image','description']
class Gallery_display(admin.ModelAdmin):
    list_display=['image']
class Sub_blog_display(admin.ModelAdmin):
    list_display=['name','image','heading1','description1','heading2','description2','heading3','description3','blog']



admin.site.register(Packages,Packages_display)
admin.site.register(Blog,Blog_display)
admin.site.register(Contact,Contact_display)
admin.site.register(Enquiry,Enquiry_display)
admin.site.register(Appointment,Appointment_display)
admin.site.register(Subpackage,Sub_package_display)
admin.site.register(Branch,Branch_display)
admin.site.register(Gallery,Gallery_display)
admin.site.register(Sub_blog,Sub_blog_display)
