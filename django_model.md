# 1.Correct Model Naming  
It is generally recommended to use singular nouns for model naming, for example: User, Post, Article. That is, the last component of the name should be a noun, e.g.: Some New Shiny Item. It is correct to use singular numbers when one unit of a model does not contain information about several objects.  

# 2.Relationship Field Naming  
For relationships such as ForeignKey, OneToOneKey, ManyToMany it is sometimes better to specify a name. Imagine there is a model called Article, - in which one of the relationships is ForeignKey for model User. If this field contains information about the author of the article, then author will be a more appropriate name than user.  

# 3.Correct Related-Name  
It is reasonable to indicate a related-name in plural as related-name addressing returns queryset. Please, do set adequate related-names. In the majority of cases, the name of the model in plural will be just right. For example:  
```  
class Owner(models.Model):
    pass
class Item(models.Model):
    owner = models.ForeignKey(Owner, related_name='items')
```  

# 4.Do not use ForeignKey with unique=True  
There is no point in using ForeignKey with unique=Trueas there exists OneToOneField for such cases.  

# 5.Attributes and Methods Order in a Model  
Preferable attributes and methods order in a model (an empty string between the points).  

* constants (for choices and other)
* fields of the model
* custom manager indication
* meta
* def __unicode__ (python 2) or def __str__ (python 3)
* other special methods
* def clean
* def save
* def get_absolut_url
* other methods  
Please note that the given order was taken from documentations and slightly expanded.  

# 6.Adding a Model via Migration  
If you need to add a model, then, having created a class of a model, execute serially manage.py commands makemigrations and migrate (or use South for Django 1.6 and below).  

# 7.Denormalisations  
You should not allow thoughtless use of denormalization in relational databases. Always try to avoid it, except for the cases when you denormalise data consciously for whatever the reason may be (e.g. productivity). If at the stage of database designing you understand that you need to denormalise much of the data, a good option could be the use of NoSQL. However, if most of data does not require denormalisation, which cannot be avoided, think about a relational base with JsonField to store some data.  

# 8.BooleanField  
Do not use null=True or blank=True for BooleanField. It should also be pointed out that it is better to specify default values for such fields. If you realise that the field can remain empty, you need NullBooleanField.  

# 9.Business Logic in Models  
The best place to allocate business logic for your project is in models, namely method models and model manager. It is possible that method models can only provoke some methods/functions. If it is inconvenient or impossible to allocate logic in models, you need to replace its forms or serializers in tasks.  

# 10.Field Duplication in ModelForm  
Do not duplicate model fields in ModelForm or ModelSerializer without need. If you want to specify that the form uses all model fields, use MetaFields. If you need to redefine a widget for a field with nothing else to be changed in this field, make use of Meta widgets to indicate widgets.  

# 11.Do not use ObjectDoesNotExist  
Using ModelName.DoesNotExist instead of ObjectDoesNotExist makes your exception intercepting more specialised, which is a positive practice.  

# 12.Use of choices  
While using choices, it is recommended to:  
* keep strings instead of numbers in the database (although this is not the best option from the point of optional database use, it is more convenient in practise as strings are more demonstrable, which allows the use of clear filters with get options from the box in REST frameworks).
* variables for variants storage are constants. That is why they must be indicated in uppercase.
* indicate the variants before the fields lists.
* if it is a list of the statuses, indicate it in chronological order (e.g. new, in_progress, completed).
* you can use Choices from the model_utils library. Take model Article, for instance:  
```  
from model_utils import Choices

class Article(models.Model):
    STATUSES = Choices(
        (0, 'draft', _('draft')),
        (1, 'published', _('published'))   )
    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    …
```

# 13.Why do you need an extra .all()?  
Using ORM, do not add an extra method call all before filter(), count(), etc.  

# 14.Many flags in a model?  
If it is justified, replace several BooleanFields with one field, status-like. e.g.  
```  
class Article(models.Model):
    is_published = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    …
```
Assume the logic of our application presupposes that the article is not published and checked initially, then it is checked and marked is_verified in True and then it is published. You can notice that article cannot be published without being checked. So there are 3 conditions in total, but with 2 boolean fields we do not have 4 possible variants, and you should make sure there are no articles with wrong boolean fields conditions combinations. That is why using one status field instead of two boolean fields is a better option: 
```  
class Article(models.Model):
    STATUSES = Choices('new', 'verified', 'published')

    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    …
```  
This example may not be very illustrative, but imagine that you have 3 or more such boolean fields in your model, and validation control for these field value combinations can be really tiresome.  

# 15.Redundant model name in a field name  
Do not add model names to fields if there is no need to do so, e.g. if table User has a field user_status - you should rename the field into status, as long as there are no other statuses in this model.  

# 16. Dirty data should not be found in a base  
Always use PositiveIntegerField instead of IntegerField if it is not senseless, because “bad” data must not go to the base. For the same reason you should always use unique,unique_together for logically unique data and never use required=False in every field.  

# 17. Getting the earliest/latest object  
You can use ModelName.objects.earliest('created'/'earliest') instead of order_by('created')[0] and you can also put get_latest_by in Meta model. You should keep in mind that latest/earliest as well as get can cause an exception DoesNotExist. Therefore, order_by('created').first() is the most useful variant.  

# 18. Never make len(queryset)  
Do not use len to get queryset’s objects amount. The count method can be used for this purpose. Like this: len(ModelName.objects.all()), firstly the query for selecting all data from the table will be carried out, then this data will be transformed into a Python object, and the length of this object will be found with the help of len. It is highly recommended not to use this method as count will address to a corresponding SQL function COUNT(). With count, an easier query will be carried out in that database and fewer resources will be required for python code performance.  

# 19. if queryset is a bad idea  
Do not use queryset as a boolean value: instead of if queryset: do something use if queryset.exists(): do something. Remember, that querysets are lazy, and if you use queryset as a boolean value, an inappropriate query to a database will be carried out.  

# 20. Using help_text as documentation  
Using model help_text in fields as a part of documentation will definitely facilitate the understanding of the data structure by you, your colleagues, and admin users.  

# 21. Money Information Storage  
Do not use FloatField to store information about the quantity of money. Instead, use DecimalField for this purpose. You can also keep this information in cents, units, etc.  

# 22. Remove _id  
Do not add _id suffix to ForeignKeyField and OneToOneField.  

# 23. Define __unicode__ or __str__  
In all non abstract models, add methods __unicode__(python 2) or __str__(python 3). These methods must always return strings.  

# 24. Transparent fields list  
Do not use Meta.exclude for a model’s fields list description in ModelForm. It is better to use Meta.fields for this as it makes the fields list transparent. Do not use Meta.fields=”__all__” for the same reason.  

# 25. Do not heap all files loaded by user in the same folder  
Sometimes even a separate folder for each FileField will not be enough if a large amount of downloaded files is expected. Storing many files in one folder means the file system will search for the needed file more slowly. To avoid such problems, you can do the following: ```  
def get_upload_path(instance, filename):
    return os.path.join('account/avatars/', now().date().strftime("%Y/%m/%d"), filename)

class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to=get_upload_path)
```  





















