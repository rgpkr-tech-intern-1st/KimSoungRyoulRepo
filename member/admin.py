from django.contrib import admin

from member.models.user_info import UserInfo, UserOwnedAddress, MileageHistory


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_num', 'owner_mileage_amount')


class UserOwnedAddressAdmin(admin.ModelAdmin):
    list_display = ('address_category', 'old_address', 'new_address', 'detail_address')


class MileageHistoryAdmin(admin.ModelAdmin):
    list_display = ('mileage_amount',)


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserOwnedAddress, UserOwnedAddressAdmin)
admin.site.register(MileageHistory, MileageHistoryAdmin)

admin.site.site_title = '김성렬 Hello Project'
admin.site.site_header = 'KimSoungRyoul Admin Page'
