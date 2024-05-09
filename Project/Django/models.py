from django.db import models

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    session_id = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    circuit_key = models.IntegerField()
    country_name = models.CharField(max_length=255)
    circuit_short_name = models.CharField(max_length=255)

class Sessions(models.Model): {
  session_id = models.AutoField(primary_key=True)
  event_id = models.IntegerField()
  session_name = models.CharField(max_length=255)
  session_type = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  start_time = models.TimeField()
  end_time = models.TimeField()
  duration = models.IntegerField()
  year = models.IntegerField()
 circuit_key = models.IntegerField()
  country_name = models.CharField(max_length=255)
  circuit_short_name = models.CharField(max_length=255)
}