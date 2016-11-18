from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import (KodeSoalModel,SoalModel,JawabanSoalModel,MataPelajaranModel)


#ModelAdmin dan ModelAdminGroup untuk Projek
# class ProjectModelAdmin(ModelAdmin):
#   model = ProjectModel
#   menu_label = 'Proyek Donasi'
#   menu_icon = 'doc-full-inverse'
  #list yang di display di page admin wagtail

  # list_display = ['title']

class KodeSoalModelAdmin(ModelAdmin):
  model = KodeSoalModel
  menu_label = 'Kode Soal'
  menu_icon = 'doc-full-inverse'
  list_display = ['kode_soal']

class MataPelajaranModelAdmin(ModelAdmin):
  model = MataPelajaranModel
  menu_label = 'Mata Pelajaran'
  menu_icon = 'doc-full-inverse'
  list_display = ['mata_pelajaran']

class JawabanSoalModelAdmin(ModelAdmin):
  model = JawabanSoalModel
  menu_label = 'Jawaban Soal'
  menu_icon = 'doc-full-inverse'
  list_display = ['jawaban_soal']

class SoalModelAdmin(ModelAdmin):
  model = SoalModel
  menu_label = 'Manajemen Soal'
  menu_icon = 'doc-full-inverse'
  list_display = ['kode_soal']

#Model untuk Event
# class EventModelAdmin(ModelAdmin):
#   model = EventModel
#   menu_label = 'Manajemen Event'
#   menu_icon = 'doc-full-inverse'
#   list_display = ['nama_event']

# class ResponseModelAdmin(ModelAdmin):
#   model = ResponseModel
#   menu_label = 'Response Kode'
#   menu_icon = 'doc-full-inverse'
#   list_display = ['kode_respon']

class SoalModelAdminGroup(ModelAdminGroup):
  menu_label = 'Bank Soal'
  menu_icon = 'folder-open-inverse'
  menu_order = 200
  items = (SoalModelAdmin,KodeSoalModelAdmin,JawabanSoalModelAdmin,MataPelajaranModelAdmin)


#
# class EventModelAdminGroup(ModelAdminGroup):
#   menu_label = 'Event'
#   menu_icon = 'folder-open-inverse'
#   menu_order = 200
#   items = (EventModelAdmin)

modeladmin_register(SoalModelAdminGroup)
