from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from sklearn.ensemble import GradientBoostingRegressor
import joblib

# Create your models here.
Smoker=(
    (0,'No'),
    (1,'Yes'),
)
class Data(models.Model):
    age=models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(70)], null=True)
    bmi=models.FloatField(null=True)
    smoker=models.PositiveIntegerField(choices=Smoker, null=True)
    children=models.PositiveIntegerField(null=True)
    predictions= models.CharField(max_length=100,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    

    def save(self, *args, **kwargs):
        ml_model=joblib.load("ml_model\ml_insurance_model.joblib")
        self.predictions= ml_model.predict([[self.age, self.bmi, self.smoker, self.children]])
        return super().save( *args, **kwargs)

    class Meta:
        ordering=["-date"]

    def __int__(self):
        return self.age
     
    
    
    