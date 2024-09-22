from django.contrib import admin 
from .models import CustomUser, Attendance, Registration, SystemInfo, Contact 
 
admin.site.register(CustomUser) 


 
 
class AttendanceAdmin(admin.ModelAdmin): 
    # Customize how the model is displayed in the admin interface if needed 
    list_display = ('trade_name', 'roll_number', 'full_name', 'attendance_status', 'attendance_date','InTime', 'OutTime','voice_points','face_points','eye_points') 
 
 
class RegistrationAdmin(admin.ModelAdmin): 
    list_display = ('registration_id', 'trade', 'roll_number', 'full_name')   
 
class SystemInfoAdmin(admin.ModelAdmin): 
    list_display = ('mac_address', 'public_ip_address', 'local_ip_address', 'latitude', 'longitude','trade','roll_number') 
 

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','message','created_at')
 
# Register the model with the admin site 
admin.site.register(Attendance, AttendanceAdmin) 
admin.site.register(Registration, RegistrationAdmin) 
admin.site.register(SystemInfo, SystemInfoAdmin)
admin.site.register(Contact, ContactAdmin)