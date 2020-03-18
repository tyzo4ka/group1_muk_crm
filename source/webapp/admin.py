from django.contrib import admin
from webapp.models import News, Announcements, Auditory, Grade, Discipline, Lesson, Schedule,\
    GroupJournal, JournalNote, JournalGrade

class JournalGradeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'journal_note', 'grade', 'student']



admin.site.register(News)
admin.site.register(Announcements)
admin.site.register(Auditory)
admin.site.register(Grade)
admin.site.register(Discipline)
admin.site.register(Lesson)
admin.site.register(Schedule)
admin.site.register(GroupJournal)
admin.site.register(JournalNote)
admin.site.register(JournalGrade, JournalGradeAdmin)
