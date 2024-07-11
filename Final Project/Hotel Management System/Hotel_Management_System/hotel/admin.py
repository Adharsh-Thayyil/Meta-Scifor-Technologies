from django.contrib import admin
from hotel.models import CouponUsers, Hotel, HotelGallery, HotelFeatures, HotelFAQs, Review, RoomServices, RoomType, Room, Booking, ActivityLog, StaffOnDuty, Coupon, Notification, Bookmark
from import_export.admin import ImportExportModelAdmin

class HotelGalleryInline(admin.TabularInline):
    model = HotelGallery

class HotelFeatures_Tab(admin.TabularInline):
    model = HotelFeatures

class HotelFAQs_Tab(admin.TabularInline):
    model = HotelFAQs

class Room_Tab(admin.TabularInline):
    model = Room

class RoomType_Tab(admin.TabularInline):
    model = RoomType

class ActivityLog_Tab(admin.TabularInline):
    model = ActivityLog

class StaffOnDuty_Tab(admin.TabularInline):
    model = StaffOnDuty

class CouponUsers_Tab(admin.TabularInline):
    model=CouponUsers

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelGalleryInline, HotelFeatures_Tab, RoomType_Tab, Room_Tab, HotelFAQs_Tab]
    list_display = ['thumbnail', 'name', 'user', 'status', 'featured', 'views']
    list_per_page=100
    search_fields=['user__username', 'name']
    list_filter=['featured','status']
    list_editable=['status']
    prepopulated_fields = {"slug": ("name",)}


class RoomAdmin(ImportExportModelAdmin):
    list_display = ['hotel' ,'room_number',  'room_type', 'price', 'number_of_beds' ,'is_available']
    list_per_page = 100


class BookingAdmin(ImportExportModelAdmin):
    inlines = [ActivityLog_Tab, StaffOnDuty_Tab]
    list_filter = [ 'hotel', 'room_type', 'check_in_date', 'check_out_date', 'is_active' , 'checked_in' ,'checked_out']
    list_display = ['booking_id', 'user', 'hotel', 'room_type', 'rooms', 'total', 'total_days', 'num_adults', 'num_children', 'check_in_date', 'check_out_date', 'is_active' , 'checked_in' ,'checked_out']
    search_fields = ['booking_id', 'user_username', 'user_email']
    list_per_page = 100


class RoomServicesAdmin(ImportExportModelAdmin):
    list_display = ['booking' ,'room', 'date', 'price', 'service_type']
    list_per_page = 100

class CouponAdmin(ImportExportModelAdmin):
    inlines = [CouponUsers_Tab]
    list_editable = ['valid_from', 'valid_to', 'active', 'type']
    list_display = ['code', 'discount', 'type', 'redemption', 'valid_from', 'valid_to' , 'active', 'date']
        
class NotificationAdmin(ImportExportModelAdmin):
    list_editable = ['seen', 'type']
    list_display = ['user', 'booking', 'type', 'seen', 'date']

class BookmarkAdmin(ImportExportModelAdmin):
    list_display = ['user','hotel']


class ReviewAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['user', 'hotel', 'review', 'reply' ,'rating', 'active']


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(RoomServices, RoomServicesAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Review, ReviewAdmin)