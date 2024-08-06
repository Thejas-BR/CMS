from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD,NAAC, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs
from .models import Announcement

# Register your models here.

class UserModel(UserAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('username', 'email', 'mobile', 'role', 'is_staff', 'is_active')

    # Optionally, define fields to be used for searching
    search_fields = ('username', 'email', 'mobile', 'role')

    # Optionally, define which fields can be filtered on
    list_filter = ('is_staff', 'is_active', 'role')

    # Optionally, define which fields are shown in detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'mobile', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Optionally, define which fields are used for adding new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'mobile', 'role', 'password1', 'password2')}
        ),
    )

admin.site.register(CustomUser, UserModel)
admin.site.register(Announcement)

"""
class UserModel(UserAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('username', 'email', 'mobile', 'is_staff', 'is_active')

    # Optionally, define fields to be used for searching
    search_fields = ('username', 'email', 'mobile')

    # Optionally, define which fields can be filtered on
    list_filter = ('is_staff', 'is_active')

    # Optionally, define which fields are shown in detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Optionally, define which fields are used for adding new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'mobile', 'password1', 'password2')}
        ),
    )

admin.site.register(CustomUser, UserModel)
"""

admin.site.register(AdminHOD)
admin.site.register(NAAC)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)

