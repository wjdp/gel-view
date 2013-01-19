from django.db import models

class GelRef(models.Model):
    prefix = models.CharField(max_length=1, default='L')
    number = models.IntegerField()
    colour = models.CharField(max_length=6,blank=True,null=True)
    colour_description = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.prefix+str(self.number)

class Gel(models.Model):
    gelref=models.ForeignKey('GelRef')
    quantity_cut = models.IntegerField()
    quantity_sheet= models.IntegerField()

    # class Meta:
    #     verbose_name = 'Gel'
    #     verbose_name_plural = 'Gels'

    def __unicode__(self):
        return self.gelref.__unicode__()
    
