from django.contrib import admin

# Register your models here.

from .models import Poll_Template, Poll_Question, Poll_Response_Sheet, Poll_Response_Answer, Poll_Question_Options

admin.site.register(Poll_Template)
admin.site.register(Poll_Question)
admin.site.register(Poll_Question_Options)
admin.site.register(Poll_Response_Sheet)
admin.site.register(Poll_Response_Answer)