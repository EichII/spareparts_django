from django.contrib import admin
from .models import SparepartCategory
from .models import Sparepart
from .models import SpmStockItem
from .models import SpmStock

@admin.register(Sparepart)
class SparepartsAdmin(admin.ModelAdmin):
    list_display = ('productcode', 'description','imagefile', 'genericprice')