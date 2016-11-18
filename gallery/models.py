from __future__ import unicode_literals

from django.db import models
#untuk dropdown di pilihan status donasi
from django import forms
import datetime
from datetime import date
from django.utils import timezone
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
  FieldPanel, TabbedInterface, ObjectList
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.views.serve import generate_signature
from django.core.urlresolvers import reverse
# randomize kode unik
from random import randint,random



#Buat link khusus image untuk di dump ke json
def generate_image_url(image, filter_spec):
    signature = generate_signature(image.id, filter_spec)
    url = reverse('wagtailimages_serve', args=(signature, image.id, filter_spec))
    image_filename = image.file.name[len('original_images/'):]
    return url + image_filename

# =========================================================================================
# ===                               KODE SOAL                                           ===
# =========================================================================================

#model untuk konten dropdown pilihan kode soal
class KodeSoalModel(models.Model):
  kode_soal = models.CharField("kode soal", max_length=128, unique=True)

  panels = [
    FieldPanel('kode_soal'),
  ]

class CategoryIterable(object):
    def __iter__(self):
        db_cat = KodeSoalModel.objects.all()
        cats = ()
        for i in db_cat:
          tup = (i.kode_soal, i.kode_soal)
          cats = (tup,) + cats
        return cats.__iter__()

cats_list = CategoryIterable()
kategori_kode_soal = forms.Select()
kategori_kode_soal.choices = cats_list

# =========================================================================================
# ===                               JAWABAN SOAL                                        ===
# =========================================================================================

class JawabanSoalModel(models.Model):
  jawaban_soal = models.CharField("jawaban soal", max_length=128, unique=True)

  panels = [
    FieldPanel('jawaban_soal'),
  ]
class CategoryIterable(object):
    def __iter__(self):
        db_cat = JawabanSoalModel.objects.all()
        cats = ()
        for i in db_cat:
          tup = (i.jawaban_soal, i.jawaban_soal)
          cats = (tup,) + cats
        return cats.__iter__()

cats_list = CategoryIterable()
pilihan_jawaban_soal = forms.Select()
pilihan_jawaban_soal.choices = cats_list

class MataPelajaranModel(models.Model):
  mata_pelajaran = models.CharField("mata pelajaran", max_length=128, unique=True)

  panels = [
    FieldPanel('mata_pelajaran'),
  ]
class CategoryIterable(object):
    def __iter__(self):
        db_cat = MataPelajaranModel.objects.all()
        cats = ()
        for i in db_cat:
          tup = (i.mata_pelajaran, i.mata_pelajaran)
          cats = (tup,) + cats
        return cats.__iter__()

cats_list = CategoryIterable()
pilihan_mata_pelajaran = forms.Select()
pilihan_mata_pelajaran.choices = cats_list


# =========================================================================================
# ===                               SOAL                                                ===
# =========================================================================================

class SoalModel (models.Model):
  kode_soal = models.CharField('kode soal', max_length=1024, default='')
  mata_pelajaran = models.CharField('mata pelajaran', max_length=1024, default='')
  detail_soal = RichTextField('detail soal',max_length=1024, default='')
  #jawaban benar
  jawaban_soal_a = RichTextField('jawaban soal a',max_length=1024, default='')
  jawaban_soal_b = RichTextField('jawaban soal b',max_length=1024, default='')
  jawaban_soal_c = RichTextField('jawaban soal c',max_length=1024, default='')
  jawaban_soal_d = RichTextField('jawaban soal d',max_length=1024, default='')
  jawaban_soal_e = RichTextField('jawaban soal e',max_length=1024, default='')
  jawaban_soal = models.CharField('jawaban soal', max_length=1024, default='')

  # gambar_soal = models.ForeignKey('wagtailimages.Image', verbose_name='Gambar Soal', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
  # gambar_soal_url = models.CharField( max_length=1024, blank=True)

  panels = [
    # FieldPanel('kode_soal'),
    FieldPanel('kode_soal',widget=kategori_kode_soal),
    FieldPanel('mata_pelajaran',widget=pilihan_mata_pelajaran),
    FieldPanel('detail_soal'),
    FieldPanel('jawaban_soal_a'),
    FieldPanel('jawaban_soal_b'),
    FieldPanel('jawaban_soal_c'),
    FieldPanel('jawaban_soal_d'),
    FieldPanel('jawaban_soal_e'),
    FieldPanel('jawaban_soal' ,widget=pilihan_jawaban_soal),
    # ImageChooserPanel('gambar_soal'),
  ]
  edit_handler = TabbedInterface([
    ObjectList(panels, heading='Soal')
  ])

  def as_dict(self):
    my_dict = {
      'kode_soal' : self.kode_soal,
      'mata_pelajaran' : self.mata_pelajaran,
      'detail_soal' : self.detail_soal,
    #   'gambar_soal_url' : self.gambar_soal_url,
      'jawaban_soal_a' : self.jawaban_soal_a,
      'jawaban_soal_b' : self.jawaban_soal_b,
      'jawaban_soal_c' : self.jawaban_soal_c,
      'jawaban_soal_d' : self.jawaban_soal_d,
      'jawaban_soal_e' : self.jawaban_soal_e,
    }
    return my_dict

  # def clean(self):
  #   super(SoalModel, self).clean
  #   if not(self.gambar_soal is None):
  #     self.gambar_soal_url = '%s' % (generate_image_url(self.gambar_soal, 'original'))



# =========================================================================================
# ===                               REFERENSI                                           ===
# =========================================================================================
class ProjectModel(models.Model):
  title = models.CharField('judul donasi',max_length=200, default='')
  description = RichTextField('description',max_length=1024, default='')
  lokasi_donasi = RichTextField('lokasi donasi', max_length=1024, default='')
  tanggal_awal_donasi = models.DateField('tanggal awal donasi', default=date.today)
  tanggal_akhir_donasi = models.DateField('tanggal akhir donasi', default=date.today)
  dana_terkumpul = models.DecimalField('dana terkumpul', max_digits=15, decimal_places=0, default=0)
  dana_dibutuhkan = models.DecimalField('dana dibutuhkan', max_digits=15, decimal_places=0, default=0)

  status_donasi = models.CharField("status donasi", max_length=128, default='status donasi belum didefinisikan')

  gallery_pic = models.ForeignKey('wagtailimages.Image', verbose_name='Gallery Pic', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
  gallery_pic_url = models.CharField( max_length=1024, blank=True)
  tag = models.CharField('tag', max_length=1024, default='')

  panels = [
    FieldPanel('title'),
    FieldPanel('description'),
    FieldPanel('lokasi_donasi'),

    FieldPanel('tanggal_awal_donasi'),
    FieldPanel('tanggal_akhir_donasi'),
    #ga perlu ditampilkan di dashboard
    #FieldPanel('dana_terkumpul'),
    FieldPanel('dana_dibutuhkan'),

    # FieldPanel('status_donasi',widget=kategori_status_donasi),

    ImageChooserPanel('gallery_pic'),
    FieldPanel('tag'),
  ]
  edit_handler = TabbedInterface([
    ObjectList(panels, heading='Project Panel')
  ])

#Nantinya dipakai untuk perhitungan donasi
  # @property
  # def my_field(self):
  #     return self.title + self.description

  def as_dict(self):
    my_dict = {
      #define field baru
      #'something' : self.myfield,
      'title' : self.title,
      'description' : self.description,
      'lokasi_donasi' : self.lokasi_donasi,
      'tanggal_awal_donasi' : self.tanggal_awal_donasi,
      'tanggal_akhir_donasi' : self.tanggal_akhir_donasi,
      'dana_terkumpul' : self.dana_terkumpul,
      'dana_dibutuhkan' : self.dana_dibutuhkan,
      'status_donasi' : self.status_donasi,
      'gallery_pic_url' : self.gallery_pic_url,
      'tag' : self.tag,
      'id': self.id,
    }
    return my_dict

  def clean(self):
    super(ProjectModel, self).clean
    if not(self.gallery_pic is None):
      self.gallery_pic_url = '%s' % (generate_image_url(self.gallery_pic, 'original'))

from django.contrib.auth.models import User

class UserProfileModel(models.Model):
  user = models.OneToOneField(User, related_name="profile")
  about = models.CharField('deskripsi', max_length=1024, default="")

class DonateModel (models.Model):
  donatur = models.ForeignKey(User, related_name="donations")
  project = models.ForeignKey(ProjectModel, related_name="donations")
  nama_donatur = models.CharField('nama donatur', max_length=1024, default='anonim')
  nilai_donasi = models.IntegerField('nilai donasi', default=0)
  status_pembayaran = models.CharField('status pembayaran', max_length=1024, default='belum terverifikasi')
  tanggal_donasi = models.DateField("tanggal donasi", default=date.today)

  @classmethod
  def create(cls, title):
    book = cls(title=title)
    # do something with the book
    return book
  #Nantinya dipakai untuk perhitungan donasi


  # @property
  # def nilai_transfer(self):
  #   kode_unik = randint(100,999)
  #   return self.nilai_donasi + kode_unik
  @property
  def nilai_transfer(self):
   kode_unik = (self.id % 1000)
   return self.nilai_donasi + kode_unik
  @property
  def kode_unik(self):
   kode_unik = (self.id % 1000)
   return kode_unik




  def as_dict(self):
    my_dict = {
      'nilai_transfer': self.nilai_transfer,
      'kode_unik': self.kode_unik,
      'nama_donatur' : self.nama_donatur,
      'nilai_donasi' : self.nilai_donasi,
      'status_pembayaran' : self.status_pembayaran,
      'tanggal_donasi' : self.tanggal_donasi,
    }
    return my_dict

class EventModel (models.Model):
  nama_event = models.CharField('nama event', max_length=1024, default='')
  deskripsi_event = RichTextField('deskripsi event',max_length=1024, default='')
  lokasi_event = RichTextField('lokasi event',max_length=1024, default='')
  tanggal_event = models.DateField("tanggal event", default=date.today)
  waktu_event_mulai = models.TimeField("waktu mulai event", default=datetime.time(07, 00))
  waktu_event_berakhir = models.TimeField("waktu akhir event", default=datetime.time(18, 00))
  gambar_event = models.ForeignKey('wagtailimages.Image', verbose_name='Gallery Pic', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
  gambar_event_url = models.CharField( max_length=1024, blank=True)
  tag_event = models.CharField('tag event', max_length=1024, default='')

  panels = [
    FieldPanel('nama_event'),
    FieldPanel('deskripsi_event'),
    FieldPanel('lokasi_event'),
    FieldPanel('tanggal_event'),
    FieldPanel('waktu_event_mulai', widget=forms.TimeInput(format='%H:%M')),
    FieldPanel('waktu_event_berakhir', widget=forms.TimeInput(format='%H:%M')),
    ImageChooserPanel('gambar_event'),
    FieldPanel('tag_event'),
  ]
  edit_handler = TabbedInterface([
    ObjectList(panels, heading='Events')
  ])

  def as_dict(self):
    my_dict = {
      'nama_event' : self.nama_event,
      'deskripsi_event' : self.deskripsi_event,
      'lokasi_event' : self.lokasi_event,
      'tanggal_event' : self.tanggal_event,
      'waktu_event_mulai' : self.waktu_event_mulai,
      'waktu_event_berakhir' : self.waktu_event_berakhir,
      'gambar_event_url' : self.gambar_event_url,
      'tag_event' : self.tag_event,
    }
    return my_dict

  def clean(self):
    super(EventModel, self).clean
    if not(self.gambar_event is None):
      self.gambar_event_url = '%s' % (generate_image_url(self.gambar_event, 'original'))

class ResponseModel(models.Model):
  kode_respon = models.CharField('kode respon', max_length=1024, default='')
  status_respon = models.CharField('kode respon', max_length=1024, default='')
  deskripsi_respon = RichTextField('deskripsi respon', max_length=1024, default='')

  panels = [
    FieldPanel('kode_respon'),
    FieldPanel('status_respon'),
    FieldPanel('deskripsi_respon'),
  ]
  edit_handler = TabbedInterface([
    ObjectList(panels, heading='Status')
  ])

  def as_dict(self):
    my_dict ={
      'kode_respon':self.kode_respon,
      'status_respon':self.status_respon,
      'deskripsi_respon':self.deskripsi_respon,
    }
    return my_dict
